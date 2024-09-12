import psycopg2
from psycopg2 import sql
import streamlit as st
from contrato import Vendas
from dotenv import load_dotenv
import os

load_dotenv()


db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

print(f"DB_HOST: {db_host}")
print(f"DB_NAME: {db_name}")
print(f"DB_USER: {db_user}")
print(f"DB_PASS: {db_pass}")


# Função para salvar os dados validados no PostgreSQL
def salvar_no_postgres(dados: Vendas):
    """
    Função para salvar no postgres
    """
    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pass,
            sslmode='require'
        )

        cursor = conn.cursor()
        
        # Inserção dos dados na tabela de vendas

        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )

        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto )
        )


        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")

    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")
        print(f"Erro completo: {e}")