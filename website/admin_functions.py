from flask import Blueprint
from flask import render_template, Response, request, flash,url_for,redirect
import re
from werkzeug.security import generate_password_hash, check_password_hash
from .models import *
from datetime import datetime
from . import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select


DB_NAME = "mess_management.db"

admin_functions = Blueprint('admin_functions', __name__)

@admin_functions.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    
    return render_template("admin-login.html", boolean=True)