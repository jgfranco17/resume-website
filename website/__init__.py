# This initializer program is used to make the entire folder a module. This allows for easier importing
# syntax and for more convenient structuring of the code.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import datetime

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    from .views import views
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    now = datetime.datetime.utcnow() + datetime.timedelta(seconds=9 * 3600)
    print(f'[{now.strftime("%d %b %Y, %I:%M:%S %p")} JST]')

    app.register_blueprint(views, url_prefix="/")
    create_database(app)
    
    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("SQLite: database created!")