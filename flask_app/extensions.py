from flask_admin import Admin
from flask_assets import Bundle, Environment
from flask_htmx import HTMX
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
migrate = Migrate()
debug_toolbar = DebugToolbarExtension()
htmx = HTMX()
admin = Admin(name="Backoffice", template_mode="bootstrap3")

assets = Environment()
assets.register("css", Bundle("src/main.css", output="dist/main.css"))
