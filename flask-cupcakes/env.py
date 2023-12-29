from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

config.set_main_option('sqlalchemy.url', current_app.config.get('SQLALCHEMY_DATABASE_URI'))