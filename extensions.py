from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from flask_htmx import HTMX

db = SQLAlchemy()
migrate = Migrate()
debug_toolbar = DebugToolbarExtension()
htmx = HTMX()
