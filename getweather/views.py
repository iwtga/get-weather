import requests
from flask import render_template, request, url_for, flash
from werkzeug.utils import redirect
from getweather import app, db
from getweather.models import City
import os

API_KEY = os.environ.get("API_KEY")

@app.route('/', method=["GET", "POST"])
@app.route('/index', method=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form('city').strip()
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}").json()
        try:
            if City.query.filter_by(city=city).first() is not None:
                flash("City Already Exists")
                return redirect(url_for('index'))
            elif data['cod'] == 200:
                c = City(city=city)
                db.session.add(c)
                db.session.commit()
                flash(f"{city} Added!")
                return redirect(url_for('index'))
            else:
                flash("Entered city not found! Please enter a valid city!")
                return redirect(url_for("index"))
        except:
            flash("Something Went Wrong!")
            return redirect(url_for("index"))
    
    cities = []
    for city in City.query.all():
        city_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city.name}&appid={API_KEY}")
        city_obj = {
            "name": city_data["name"],
            "desc": ", ".join(i["description"] for i in city_data["weather"]),
            "temp": city_data["main"]["temp"]
        }
        cities.append(city_obj)
    return render_template(url_for('index'), cities=cities)