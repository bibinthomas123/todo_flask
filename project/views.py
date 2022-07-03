from flask import flash, render_template, Blueprint, url_for, request
from .model import User ,Note
from flask_sqlalchemy import SQLAlchemy
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required,  current_user


views = Blueprint('views', __name__)


@views.route("/",  methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            # flash('Note added!', category='success')
    return render_template("todo.html", user=current_user)


# @views.route("/todo")
# def todo():
#     return render_template("todo.html")
