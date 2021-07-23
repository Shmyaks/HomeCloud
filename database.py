from app import db, login_manager
from flask_login import UserMixin, current_user
from datetime import datetime


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    pc_name = db.Column(db.String(32))
    password = db.Column(db.String(256))


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
