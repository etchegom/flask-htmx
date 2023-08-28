from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="dev")

DEBUG = ENV == "dev"
FLASK_DEBUG = ENV == "dev"
FLASK_APP = "flask-htmx-tailwindcss"
SECRET_KEY = env.str("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False

FLASK_ADMIN_SWATCH = "cerulean"
