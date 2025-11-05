import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///catalogo.db")

# Class para Teste com Pytest
class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DATABASE_URI = 'sqlite:///:memory:'