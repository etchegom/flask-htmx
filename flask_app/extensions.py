from flask_assets import Bundle, Environment
from flask_htmx import HTMX
from flask_migrate import Migrate
from flask_security import Security
from flask_sqlalchemy import SQLAlchemy

from flask_debugtoolbar import DebugToolbarExtension
from flask_marshmallow import Marshmallow
from flask_restx import Api

db = SQLAlchemy()
security = Security()
migrate = Migrate()
debug_toolbar = DebugToolbarExtension()
htmx = HTMX()
api = Api()
ma = Marshmallow()

assets = Environment()
assets.register("css", Bundle("src/main.css", output="dist/main.css"))
