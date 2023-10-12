import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
    BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
