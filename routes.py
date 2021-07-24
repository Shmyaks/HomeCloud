from flask_login.utils import login_required
from app import app
from flask import render_template, request, redirect, flash, abort, jsonify, send_file
# from database import Users,
import random
from flask_login import login_user, current_user
from datetime import datetime, timedelta
import os


@app.route('/videos', methods=['GET'])
def view_videos():
    """Роут отвечает за видео"""

    return render_template('home.html')


@app.route('/settings', methods=['GET'])
def view_setting():
    """Роут отвечает за видео"""

    return render_template('settings.html')
