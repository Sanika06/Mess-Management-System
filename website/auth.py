from flask import Blueprint
from flask import Flask, render_template, Response, request, session, flash,url_for,redirect
import re
from werkzeug.security import generate_password_hash, check_password_hash
from .models import student_info,Attendance
from . import db
from flask_session import Session


auth = Blueprint('auth', __name__)

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@auth.route('/user-login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        MIS = request.form.get('MIS')
        password = request.form.get('password')
        students = student_info.query.all()
        for stud in students:
            print(stud.MIS)
            if MIS in stud.MIS:
                if(check_password_hash(stud.Password, password)):
                    session["name"] = request.form.get("MIS")
                    return redirect("/user-dashboard")
        
    return render_template("user-login.html", boolean=True)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        MIS = request.form.get('MIS')
        year = request.form.get('year')
        phone_no = request.form.get('phoneno')
        room_no=request.form.get('roomno')
        password = request.form.get('Password')

        flag = 0
        if len(MIS) < 9 or len(MIS) > 9:
            flash('Invalid MIS', category="error")
        elif len(phone_no) < 10 or len(phone_no) > 10:
            flash('Invalid phone no', category="error")            
        elif len(password) < 6:
            for i in password:
                if i.isupper():
                    flag = flag + 1
                elif i.islower():
                    flag = flag + 1
                elif(bool(re.match('^[a-zA-Z0-9]*$', password)) == True):
                    flag = flag + 1
            if flag != 3:
                flash("InValid password", category="error")
    
        else:
          
            new_student=student_info(Name=name,MIS=MIS,Phone_no=phone_no,year=year,Room_no=room_no,Password=generate_password_hash(password,method='sha256'))
            db.session.add(new_student)
            db.session.commit()
            flash('Account created!',category='success')
            return redirect(url_for('auth.login'))

    return render_template("register.html", boolean=True)

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")