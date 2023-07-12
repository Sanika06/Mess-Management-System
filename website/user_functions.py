from flask import Blueprint
from flask import render_template, Response, session, request, flash,url_for,redirect
import re
from werkzeug.security import generate_password_hash, check_password_hash
from .models import *
from datetime import datetime
from . import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select


DB_NAME = "mess_management.db"

user_functions = Blueprint('user_functions', __name__)

@user_functions.route('/attendance', methods=['GET', 'POST'])
def mark_absent():
    user_MIS=session["name"]
    today = datetime.now()
    year = today.year
    month = today.month
    date = today.day
    lunch=""
    dinner=""
    if request.method == 'POST':
        meal_time = request.form.getlist('meal_time')
        if(len(meal_time) > 1):
            if(meal_time[0] == 'Lunch'):
                lunch = date
            if(meal_time[1] == 'Dinner'):
                dinner = date
                print(date)
        elif(len(meal_time) == 1):
            if(meal_time[0] == 'Lunch'):
                lunch = date
                
            if(meal_time[0] == 'Dinner'):
                dinner = date
                print(date)

        
        
        mark_absent=Attendance(user_MIS=user_MIS, Year=year, Month = month, Lunch = lunch, Dinner = dinner)
        db.session.add(mark_absent)
        db.session.commit()
        flash('Absentee Marked',category='success')
        return redirect(url_for('views.user_dashboard'))
#        print("hillow semika")
    return render_template("mark_absentee.html", boolean=True)




@user_functions.route('/present')
def present_records():
    students = student_info.query.filter(student_info.MIS == session["name"])
    attendees = Attendance.query.filter(Attendance.user_MIS == session["name"])

    return render_template('present_records.html', curr_name = session["name"], dataOfStudents=students,data_of_absentees=attendees)


@user_functions.route('/payment')
def payment_records():
    # Fetch data using SQLAlchemy
    # data = select(student_info.Name).where(student_info.Name == "onkar")

    students = student_info.query.all()
    attendees = Attendance.query.all()
    # payment=Payment.query.all()
    # i=0
    # std=0
    # count=0
    # while(i<31):
    #     if attendees[std].Lunch == 'P':
    #         count=count+1
    #     if attendees[std].Dinner == 'P':
    #         count=count+1
        
    # payment_rec=Payment(user_MIS=students.MIS, noOfMeals = count, total = count*50)
    # db.session.add(payment_rec)
    # db.session.commit()
        # data = session.query(student_info).all()
        
        # Pass the data to the HTML template and render it
    return render_template('payment_records.html', data=students,data_of_absentees=attendees)



