PGDMP                      {            sepatu    16.0    16.0 	    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24781    sepatu    DATABASE     }   CREATE DATABASE sepatu WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';
    DROP DATABASE sepatu;
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    4            �            1259    24782    data_sepatu    TABLE     �   CREATE TABLE public.data_sepatu (
    "No" character varying NOT NULL,
    "Merk_Sepatu" character varying,
    "Harga" integer,
    "Kualitas_Material" integer,
    "Desain" integer,
    "Kenyamanan" integer,
    "Durabilitas" integer
);
    DROP TABLE public.data_sepatu;
       public         heap    postgres    false    4            �          0    24782    data_sepatu 
   TABLE DATA              COPY public.data_sepatu ("No", "Merk_Sepatu", "Harga", "Kualitas_Material", "Desain", "Kenyamanan", "Durabilitas") FROM stdin;
    public          postgres    false    215   �       P           2606    24820    data_sepatu data_sepatu_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.data_sepatu
    ADD CONSTRAINT data_sepatu_pkey PRIMARY KEY ("No");
 F   ALTER TABLE ONLY public.data_sepatu DROP CONSTRAINT data_sepatu_pkey;
       public            postgres    false    215            �   m   x�U�A
A�Տ��L2�{����'�����L��M�b\���mZ9�Ď"�.����5x��BQ��w冪��j?WF΃a_��q��M5�1�J��Ͳ�I�6     