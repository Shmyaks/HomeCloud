from flask_login.utils import login_required
from app import app, scheduler, db
from flask import render_template, request, redirect, flash, abort, jsonify, send_file
from database import Groups, Users, Exam, Ticket, Question, Answers, stdnsINFO, GroupSheets
import random
from flask_login import login_user, current_user
from datetime import datetime, timedelta
import os
