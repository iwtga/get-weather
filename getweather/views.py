import requests
from flask import render_template, request, url_for, flash, redirect
from getweather import app
import os

API_KEY = os.environ.get("API_KEY")

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form('city').strip()
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}").json()
    return render_template('index.html')