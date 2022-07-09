from flask import flash, render_template, Blueprint, request , jsonify
from .model import User ,Note
from flask_sqlalchemy import SQLAlchemy
from . import db
from flask_login import login_required,  current_user
import json
from time import sleep

views = Blueprint('views', __name__)


@views.route("/",  methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('todo')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            print(note)
            # flash('Note added!', category='success')
    return render_template("todo.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    sleep(0.7)
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})