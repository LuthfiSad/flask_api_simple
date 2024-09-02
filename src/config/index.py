import os
from dotenv import load_dotenv
load_dotenv()

Envrolment = {
    "SECRET_KEY": os.getenv('SECRET_KEY'),
    "DB_URL": os.getenv('DB_URL')
}