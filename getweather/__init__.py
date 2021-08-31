from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

from getweather import views