from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import os
# from os import getenv
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://eash:Eashdino10@appdatabase.cafuawxxfbj2.eu-west-1.rds.amazonaws.com:3306/database_project'
app.config['SECRET_KEY'] = "MY_SECRET_KEY"


db = SQLAlchemy(app)


from application import routes
