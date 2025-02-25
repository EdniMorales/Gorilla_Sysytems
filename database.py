import mysql.connector as mysql
import sqlite3 as sqlite

from dotenv import load_dotenv
from decouple import config
from pathlib import Path

class DataBase:
    def __init__(self, type_connection: str):
        """Coneccion a la base de datos.

        Seleccione el tipo de coneccion que se va a realizar

        Args:
            Mysql (str): Configurar para base de datos de MySQL

            Sqlite (str): Configurar para base de datos de SQLite

        """
        env_path = Path(__file__).resolve().parent / 'settings.env'
        load_dotenv(env_path)
        try:
            match type_connection:
                case "Mysql":
                    ...
                case "Sqlite":
                    ...
                case _:
                    raise ValueError("Configuracion no valida")
        except:
            ...
