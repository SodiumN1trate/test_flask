from settings import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

_metadata = MetaData(naming_convention=convention)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AutoNomasDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app, metadata=_metadata)

# Migrate
migrate = Migrate(app, db)

class RentalPoint(db.Model):
    __tablename__ = 'rental_point'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String(25), nullable=False)
    car = db.relationship("Car", cascade="all, delete")

    def __repr__(self):
        return '<RentalPoint %r>' % (self.title)

    def serialize(self):
        return {"id": self.id,
                "title": self.title,
                "city": self.city,
                "address": self.address
                }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(5), nullable=False)
    car = db.relationship("UserCar", cascade="all, delete")

    def __repr__(self):
        return '<User %r>' % (self.firstname)


class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    manufacture = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    classifications = db.Column(db.String(15), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    number_plate = db.Column(db.String(10), nullable=False)
    hourly_rate = db.Column(db.Integer, nullable=False)
    from_date = db.Column(db.DateTime, nullable=False)
    to_date = db.Column(db.DateTime, nullable=False)
    reservation = db.relationship("UserCar", cascade="all, delete")
    rental_point_id = db.Column(db.Integer, db.ForeignKey("rental_point.id"))

    def __repr__(self):
        return '<Car %r %r>' % (self.manufacture , self.id)

    def serialize(self):
        return {"id": self.id,
                "manufacture": self.manufacture,
                "rental_point": "",
                "model": self.model,
                "classifications": self.classifications,
                "year": self.year,
                "number_plate": self.number_plate,
                "hourly_rate": self.hourly_rate,
                "from_date": self.from_date,
                "to_date": self.to_date,
                "rental_point_id": self.rental_point_id
                }

class UserCar(db.Model):
    __tablename__ = 'user_car'
    id = db.Column(db.Integer, primary_key=True)
    from_date = db.Column(db.DateTime, nullable=False)
    to_date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    reservation_number = db.Column(db.Integer, primary_key=True)
    booked_status = db.Column(db.Integer, default=0)
    car_id = db.Column(db.Integer, db.ForeignKey("car.id"))
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return '<UserCar %r %r>' % (self.car , self.id)
