PGDMP  "    0            	    {            database_sepatu    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16404    database_sepatu    DATABASE     �   CREATE DATABASE database_sepatu WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Indonesian_Indonesia.1252';
    DROP DATABASE database_sepatu;
                postgres    false            �            1259    16405    data_sepatu    TABLE     �   CREATE TABLE public.data_sepatu (
    "No" integer NOT NULL,
    "Merk_Sepatu" "char",
    "Harga" integer,
    "Kualitas_Material" "char",
    "Desain" "char",
    "Kenyamanan" "char",
    "Durabilitas" "char"
);
    DROP TABLE public.data_sepatu;
       public         heap    postgres    false            �          0    16405    data_sepatu 
   TABLE DATA              COPY public.data_sepatu ("No", "Merk_Sepatu", "Harga", "Kualitas_Material", "Desain", "Kenyamanan", "Durabilitas") FROM stdin;
    public          postgres    false    215   /                  2606    16409    data_sepatu data_sepatu_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.data_sepatu
    ADD CONSTRAINT data_sepatu_pkey PRIMARY KEY ("No");
 F   ALTER TABLE ONLY public.data_sepatu DROP CONSTRAINT data_sepatu_pkey;
       public            postgres    false    215            �   e   x�]�A
�0ϻ��TMk�*xQ����aZ[��ð�����#������^�V�8�2Ho��R��R�z�R�:l�>�Z����|~+�jH�*VL     