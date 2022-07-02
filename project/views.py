
from django.shortcuts import redirect
from flask import flash, render_template, Blueprint, url_for, request
from .model import User
from flask_sqlalchemy import SQLAlchemy
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


views = Blueprint('views', __name__)


@views.route("/")
def home():
    return "<h1>hello</h1>" 

@views.route("/todo")
def todo():
    return render_template("todo.html")
