from time import sleep
from flask import Blueprint, render_template, request, flash, redirect, url_for, flash
from .model import  User,Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError
import re 


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("user_name")
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                print("passed checking")
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
                print("error password")
        else:
            flash('Username does not exist.', category='error')
            print("error")

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required  
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    pattern ="(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[!?@])[a-zA-Z0-9!?@]{8,}" 
    if request.method == "POST":
        firstname = request.form.get("new_full_name")
        username = request.form.get("new_user_name")
        password = request.form.get("new_password")

        user = User.query.filter_by(username=username).first()
        # if user:
        #     flash('username already exists.', category='error')
        if len(firstname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        if (re.search(pattern,password)):
            try:
                new_user = User(username=username, password=generate_password_hash(password, method='sha256'), first_name=firstname)
                db.session.add(new_user)
                db.session.commit()
                print("added user")
                login_user(new_user, remember=True)
                flash('Account created!', category='success')
                return redirect(url_for('views.home'))
            except IntegrityError:
                db.session.rollback()
                return f'<h1> the username "{user.username}" is already taken</h1>'
        else:
            flash('Weak Password !! Try again', category='error')
    return render_template("create_Acc.html")
