from flask_login.utils import login_required
from app import app, db
from flask import render_template, request, redirect, flash, abort, jsonify, send_file
from database import Directoryes
import random
from flask_login import login_user, current_user
from datetime import datetime, timedelta
import os


@app.route('/videos/', methods=['GET'])
def view_videos():
    """Роут отвечает за видео"""
    page = 0 if not request.args.get('page') else request.args.get('page')
    
    filter = (None == None) if not request.args.get(
        'path_id') else (Directoryes.id == request.args.get('path_id'))

    path = Directoryes.query.filter(filter).first_or_404('path does not exist')

    for root, dirs, files in os.walk(path.path):
        for filename in files:
            print(filename)

    paths = db.session.query(Directoryes.path).all()

    return render_template('home.html', paths = paths)


@app.route('/settings', methods=['GET'])
def view_setting():
    """Роут отвечает за настройки"""
    paths = Directoryes.query.all()


    return render_template('settings.html', paths=paths)


@app.route('/path', methods=['POST'])
def create_path():
    """Роут отвечает за создания путя"""
    path = Directoryes(path = request.form['path'])

    db.session.add(path)
    db.session.commit()

    return 'ok'


@app.route('/path/<int:id>', methods=['DELETE'])
def delete_patg(id):
    """Роут отвечает за удаления путя"""
    path = Directoryes.query.filter_by(id = id).first_or_404('path does not exists')

    db.session.delete(path)
    db.session.commit()

    return 'ok'
