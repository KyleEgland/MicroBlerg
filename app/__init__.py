#! python
#
# MicroBlerg
# The init file for another microblog tutorial.
from config import Config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importing routes here is a workaround to avoid circular imports; the routes
# module imports the app variable defined in this script.
from app import routes, models
