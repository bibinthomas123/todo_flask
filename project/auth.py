from flask import Blueprint, render_template, request, flash, redirect, url_for
from .model import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        firstname =request.form.get("new_first_name")
        username = request.form.get("new_user_name")
        password = request.form.get('new_password')

        # user = User.query.filter_by(email=email).first()
        # if user:
        #     if check_password_hash(user.password, password):
        #         flash('Logged in successfully!', category='success')
        #         login_user(user, remember=True)
        #         return redirect(url_for('views.home'))
        #     else:
        #         flash('Incorrect password, try again.', category='error')
        # else:
        #     flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
            firstname = request.form.get("new_full_name")
            username = request.form.get("new_user_name")
            password = request.form.get("new_password")

            # user = User.query.filter_by(email=email).first()
            # if user:
            #     flash('Email already exists.', category='error')
            if len(firstname) < 2:
                flash('First name must be greater than 1 character.', category='error')
            elif len(password) < 7:
                flash('Password must be at least 7 characters.', category='error')
            else:
                new_user = User(username=username, password=generate_password_hash(password, method='sha256'),first_name=firstname)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created!', category='success')
                return redirect(url_for('views.home'))
    return render_template("create_Acc.html")
