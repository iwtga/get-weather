from flask import render_template
from getweather import app

@app.route('/')
def index():
    return "Hello World"