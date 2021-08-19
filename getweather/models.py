from getweather import app, db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f'<City {self.city}'