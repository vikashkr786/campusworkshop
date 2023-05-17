"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7geu4dadc9vlta3d0-a",
        database="todo_f5ph",
        user="todo_f5ph_user",
        password="7PE862h3hHogZ31VD9UuHcGrpoJMCx5o")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
