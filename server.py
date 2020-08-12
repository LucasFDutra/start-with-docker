from flask import Flask, jsonify
import os
import psycopg2


def create_table():
    connection_params = {
        'dbname': 'flask_db',
        'user': 'postgres',
        'password': 'superSenha',
        'host': 'db',
        'port': '5432'
    }
    connection = psycopg2.connect(**connection_params)

    cursor = connection.cursor()

    cursor.execute("""
            CREATE TABLE users (
            id_user_pk TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            avatar TEXT NOT NULL,
            whatsapp TEXT NOT NULL,
            bio TEXT NOT NULL
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()


app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello'


@app.route('/create')
def create():
    create_table()
    return 'Tabela criada com sucesso'


os.environ['FLASK_ENV'] = "development"
app.run(host='0.0.0.0', port=5000)
