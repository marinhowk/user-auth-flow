from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

class BancoDeDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD,
            database = DB_NAME
        )

    def get_conexao(self):
        return self.conexao