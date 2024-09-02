import os
from .index import Envrolment 

class Config:
    # Atur konfigurasi database MySQL Anda di sini
    SQLALCHEMY_DATABASE_URI = Envrolment['DB_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)