
from http import HTTPStatus
from flask import Flask, request, abort
from flask_restful import Resource, Api 
from models import Sepatu as ModelSepatu
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session

session = Session(engine)

app = Flask(__name__)
api = Api(app)        

class BaseMethod():

    def __init__(self):
        self.raw_weight = {'Harga': 5, 'Kualitas_Material': 5, 'Desain': 5, 'Kenyamanan': 5, 'Durabilitas': 5}

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v/total_weight, 2) for k, v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(ModelSepatu.No, ModelSepatu.Merk_Sepatu, ModelSepatu.Harga, ModelSepatu.Kualitas_Material, ModelSepatu.Desain, ModelSepatu.Kenyamanan, ModelSepatu.Durabilitas)
        result = session.execute(query).fetchall()
        print(result)
        return [{'No': data_sepatu.No, 'Merk_Sepatu': data_sepatu.Merk_Sepatu, 'Harga': data_sepatu.Harga, 'Kualitas_Material': data_sepatu.Kualitas_Material, 'Desain': data_sepatu.Desain, 'Kenyamanan': data_sepatu.Kenyamanan, 'Durabilitas': data_sepatu.Durabilitas} for data_sepatu in result]

    @property
    def normalized_data(self):
        Harga_values = []
        Kualitas_Material_values = []
        Desain_values = []
        Kenyamanan_values = []
        Durabilitas_values = []

        for data in self.data:
            Harga_values.append(data['Harga'])
            Kualitas_Material_values.append(data['Kualitas_Material'])
            Desain_values.append(data['Desain'])
            Kenyamanan_values.append(data['Kenyamanan'])
            Durabilitas_values.append(data['Durabilitas'])

        return [
            {'No': data['No'],
             'Merk_Sepatu': data['Merk_Sepatu'],
             'Harga': min(Harga_values) / data['Harga'] ,
             'Kualitas_Material': data['Kualitas_Material'] / max(Kualitas_Material_values),
             'Desain': data['Desain'] / max(Desain_values),
             'Kenyamanan': data['Kenyamanan'] / max(Kenyamanan_values),
             'Durabilitas': data['Durabilitas'] / max(Durabilitas_values)
             }
            for data in self.data
        ]

    def update_weights(self, new_weights):
        self.raw_weight = new_weights

class WeightedProductCalculator(BaseMethod):
    def update_weights(self, new_weights):
        self.raw_weight = new_weights

    @property
    def calculate(self):
        normalized_data = self.normalized_data
        produk = []

        for row in normalized_data:
            product_score = (
                row['Harga'] ** self.raw_weight['Harga'] *
                row['Kualitas_Material'] ** self.raw_weight['Kualitas_Material'] *
                row['Desain'] ** self.raw_weight['Desain'] *
                row['Kenyamanan'] ** self.raw_weight['Kenyamanan'] *
                row['Durabilitas'] ** self.raw_weight['Durabilitas'] 
            )

            produk.append({
                'No': row['No'],
                'produk': product_score
            })

        sorted_produk = sorted(produk, key=lambda x: x['produk'], reverse=True)

        sorted_data = []

        for product in sorted_produk:
            sorted_data.append({
                'No': product['No'],
                'score': product['produk']
            })

        return sorted_data


class WeightedProduct(Resource):
    def get(self):
        calculator = WeightedProductCalculator()
        result = calculator.calculate
        return result, HTTPStatus.OK.value
    
    def post(self):
        new_weights = request.get_json()
        calculator = WeightedProductCalculator()
        calculator.update_weights(new_weights)
        result = calculator.calculate
        return {'data': result}, HTTPStatus.OK.value
    

class SimpleAdditiveWeightingCalculator(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        result = {row['No']:
                  round(row['Harga'] * weight['Harga'] +
                        row['Kualitas_Material'] * weight['Kualitas_Material'] +
                        row['Desain'] * weight['Desain'] +
                        row['Kenyamanan'] * weight['Kenyamanan'] +
                        row['Durabilitas'] * weight['Durabilitas'], 2)
                  for row in self.normalized_data
                  }
        sorted_result = dict(
            sorted(result.items(), key=lambda x: x[1], reverse=True))
        return sorted_result

    def update_weights(self, new_weights):
        self.raw_weight = new_weights

class SimpleAdditiveWeighting(Resource):
    def get(self):
        saw = SimpleAdditiveWeightingCalculator()
        result = saw.calculate
        return result, HTTPStatus.OK.value

    def post(self):
        new_weights = request.get_json()
        saw = SimpleAdditiveWeightingCalculator()
        saw.update_weights(new_weights)
        result = saw.calculate
        return {'data': result}, HTTPStatus.OK.value


class Sepatu(Resource):
    def get_paginated_result(self, url, list, args):
        page_size = int(args.get('page_size', 10))
        page = int(args.get('page', 1))
        page_count = int((len(list) + page_size - 1) / page_size)
        start = (page - 1) * page_size
        end = min(start + page_size, len(list))

        if page < page_count:
            next_page = f'{url}?page={page+1}&page_size={page_size}'
        else:
            next_page = None
        if page > 1:
            prev_page = f'{url}?page={page-1}&page_size={page_size}'
        else:
            prev_page = None
        
        if page > page_count or page < 1:
            abort(404, description=f'Halaman {page} tidak ditemukan.') 
        return {
            'page': page, 
            'page_size': page_size,
            'next': next_page, 
            'prev': prev_page,
            'Results': list[start:end]
        }

    def get(self):
        query = select(ModelSepatu)
        data = [{'No': data_sepatu.No, 'Merk_Sepatu': data_sepatu.Merk_Sepatu, 'Harga': data_sepatu.Harga, 'Kualitas_Material': data_sepatu.Kualitas_Material, 'Desain': data_sepatu.Desain, 'Kenyamanan': data_sepatu.Kenyamanan, 'Durabilitas': data_sepatu.Durabilitas} for data_sepatu in session.scalars(query)]
        return self.get_paginated_result('data_sepatu/', data, request.args), HTTPStatus.OK.value


api.add_resource(Sepatu, '/data_sepatu')
api.add_resource(WeightedProduct, '/wp')
api.add_resource(SimpleAdditiveWeighting, '/saw')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
