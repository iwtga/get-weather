import requests
from flask import render_template, request, url_for, flash
from werkzeug.utils import redirect
from getweather import app, db
from getweather.models import City

@app.route('/', method=["GET", "POST"])
@app.route('/index', method=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form('city')
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dc34755a51fe4175feca0b7eca4b7219").json()
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
    return render_template(url_for('index'))