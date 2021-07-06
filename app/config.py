from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/weather'
app.config['SECRET_KEY'] = 'this is very secret!!!'
db = SQLAlchemy(app)
api = Api(app)
