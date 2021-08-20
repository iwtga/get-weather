import requests
from flask import render_template, request
from getweather import app

@app.route('/', method=["GET", "POST"])
def index():
    if request.method == "POST":
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={request.form('city')}&appid=dc34755a51fe4175feca0b7eca4b7219").json()
    return render_template('index.html')