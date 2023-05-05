"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaajhak728r886nt7qg-a.oregon-postgres.render.com",
        database="todo054",
        user="root",
        password="VxlT6Ar71iJxi7ttu1Q7Y3Rey099h8CL")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
