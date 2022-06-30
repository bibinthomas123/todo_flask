from flask_sqlalchemy import SQLAlchemy
from flask import render_template ,Blueprint,url_for,request

views = Blueprint('views', __name__)



db = SQLAlchemy(app)
class UserData(db.model):
    


@views.route("/")
def create_account():
    return render_template("create_Acc.html")

@views.route("/login",methods=["POST"])
def login():
    return render_template("login.html")

@views.route("/todo")
def todo():
    return render_template("todo.html")