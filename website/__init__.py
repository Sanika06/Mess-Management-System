from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db =  SQLAlchemy()
DB_NAME = "mess_management.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] ="MALIKA_E_DUMNUM"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .user_functions import user_functions
    from .admin_functions import admin_functions

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    app.register_blueprint(user_functions,url_prefix='/')
    app.register_blueprint(admin_functions,url_prefix='/')

    from .models import student_info,Attendance
    create_db(app)
    return app

def create_db(app):
    if not path.exists('website/' +DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database')
    return