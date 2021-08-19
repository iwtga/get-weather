from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/main.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


from getweather import views, models