from django.shortcuts import render
from flask import render_template ,Blueprint


views = Blueprint('views', __name__)

@views.route("/")
def create_account():
    return render_template("create_Acc.html")

@views.route("/login")
def login():
    return render_template("login.html")

@views.route("/todo")
def todo():
    return render_template("todo.html")