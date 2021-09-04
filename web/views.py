# This file houses the different web views accessible from the main host domain.

from flask import Blueprint, render_template, request, redirect, url_for, flash
import datetime
from flask.helpers import flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from .addons import TimeFunction
from .general import timeformat, timestamp, months_list, colors
import calendar

views = Blueprint("views", __name__)
db = SQLAlchemy()
DB_NAME = "database.db"
SITENAME = "Chino\'s Resume"
times = TimeFunction(9)


@views.route("/home")
def home():
    return render_template("home.html", login_time=times.timestamps('minute'), site_name=SITENAME)


@views.route("/")
@views.route("/index")
@views.route("/welcome")
def mainpage():
    return render_template("welcome.html", user=current_user, site_name=SITENAME)


# Error Handling Pages
@views.route("/error")
def error():
    return render_template("500.html")
