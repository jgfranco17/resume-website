# This initializer program is used to make the entire folder a module. This allows for easier importing
# syntax and for more convenient structuring of the code.

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"
SITENAME = "Writing Room"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix="/")


    @app.errorhandler(404)
    def invalid_url(e):
        return render_template("404.html")

    @app.errorhandler(405)
    def not_allowed(e):
        return render_template("405.html")

    @app.errorhandler(500)
    def internal_error(e):
        return render_template("500.html")

    return app

