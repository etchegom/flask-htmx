"""Flask App configuration."""

from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    ENVIRONMENT = "dev"
    FLASK_APP = "flask-htmx-tailwindcss"
    FLASK_DEBUG = True
    SECRET_KEY = environ.get("SECRET_KEY")
