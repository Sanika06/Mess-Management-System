from flask import Blueprint, render_template, session, redirect
from .models import student_info

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')


@views.route('/user-dashboard')
def user_dashboard():
    if 'name' in session:
        students = student_info.query.all()
        return render_template('user_dashboard.html', data=students)
    return redirect('/login')

@views.route('/committee')
def committee():
    return render_template('committee.html')



