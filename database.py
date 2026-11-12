import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def obtenir_connexion():

    variables = [
        "DB_NAME",
        "DB_USER",
        "DB_PASSWORD",
        "DB_HOST",
        "DB_PORT"
    ]

    for variable in variables:
        if not os.getenv(variable):
            raise ValueError(
                f"La variable {variable} est absente du fichier .env"
            )

    connexion = psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    return connexion