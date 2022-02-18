from models import db, UserCar, User, Car, RentalPoint 
from flask import session
from datetime import datetime

def save_car_booking(data, id):
    car = UserCar(
        car=data['car'],
        from_date=data['from_date'],
        to_date=data['to_date'],
        price=0.0,
        owner_id=id
    )
    db.session.add(car)
    db.session.commit()

def get_user_car_booking(id):
    cars = UserCar.query.filter(UserCar.owner_id == id).all()
    if cars != None:
        return cars
    else:
        raise Exception('Lūdzu pieslēdzaties!')

def save_user_registration(data):
    email_exist = (User.query.filter(User.email == data['email']).first() != None)
    if email_exist == False:
        if data['password'] == data['password_confirm']:
            user = User(
                firstname=data['firstname'],
                lastname=data['lastname'],
                email=data['email'],
                password=data['password'],
                address=data['address'],
                mobile_number=data['mobile_number'],
                role="user"
            )
            db.session.add(user)
            db.session.commit()
            session['user'] = user.id
            return True
        else:
            raise Exception('Paroles nesakrīt!')
    elif email_exist == True and data['password'] != data['password_confirm']:
        raise Exception('Paroles nesakrīt un E-pasts ir aizņemts!')
    else:
        raise Exception('E-pasts ir aizņemts!')

def compare_user_login(data):
    user = User.query.filter(User.email == data['email']).first() # Iegūstam lietotāju kuram ir ievadītais e-pasts
    if user != None and user.password == data['password']:
        session['user'] = user.id
        return True
    else:
        raise Exception("Nepareizs epasts vai parole!")

def get_user_data(id):
    return User.query.filter(User.id == id).first()

def get_all_users_cars():
    data = []
    for car in UserCar.query.all():
        data.append([car, get_user_data(car.owner_id)])
    return data


def is_user_admin(id):
    '''returno True, ja lietotājs ir admins'''
    try:
        return True if get_user_data(id).role == "admin" else False
    except Exception as e:
        raise Exception("Lietotajs nav piefdfsdfdsslēdzies sistēmai/Nav pieeja šai lapai")

def is_user_logged():
    try:
        return True if get_user_data(session['user']) else False
    except:
        raise Exception("Lietotajs nav pieslēdzies sistēmai/Nav pieeja šai lapai")

def set_status_code(car_id, status_code):
    try:
        UserCar.query.get(car_id).booked_status = status_code
        db.session.commit()
        return UserCar
    except:
        raise Exception("Notika kļūda!")


def remove_car(id):
    try:
        car_id = UserCar.query.filter(UserCar.id == id).first()
        print(car_id.id)
        db.session.delete(car_id)
        db.session.commit()
        return True
    except:
        raise Exception("Notika kļūda!")

def get_cars():
    return Car.query.all()

def get_unique_car_models_by_manufacture(manufacture):
    cars = Car.query.filter(Car.manufacture == manufacture).all()
    models = []
    for car in cars:
        if car.model not in models:
            models.append(car.model)
    return models

def get_unique_manufactures():
    manufactures = []
    for car in Car.query.all():
        if car.manufacture not in manufactures:
            manufactures.append(car.manufacture)
    return manufactures

def set_new_rental_point(data):
    try:
        rental_point = RentalPoint(
            title=data['title'],
            city=data['city'],
            address=data['address']
            )
        db.session.add(rental_point)
        db.session.commit()
        return rental_point
    except:
        raise Exception("Notika kļūda!")

def get_all_rental_points():
    return RentalPoint.query.all()

def get_rental_point(id):
    return RentalPoint.query.filter(RentalPoint.id == id).first()

def get_rental_point_car(id):
    return Car.query.filter(Car.id == id).first()


def get_rental_point_cars(id):
    return Car.query.filter_by(rental_point_id=id).all() 

def delete_rental_point(id):
    try:
        db.session.delete(get_rental_point(id))
        db.session.commit()
        return True
    except:
        raise Exception("Notika kļūda!")

def delete_rental_point_car(id):
    try:
        db.session.delete(Car.query.filter(Car.id==id).first())
        db.session.commit()
        return True
    except:
        raise Exception("Notika kļūda!")

def edit_rental_point(id, data):
    try:
        rental_point = get_rental_point(id)
        rental_point.title = data['title']
        rental_point.city = data['city']
        rental_point.address = data['address']
        db.session.commit()
    except:
        raise Exception("Notika kļūda!")

def edit_rental_point_detail(id, data):
    try:
        rental_point_edit_car = get_rental_point_car(id)
        rental_point_edit_car.manufacture = data['manufacture']
        rental_point_edit_car.model = data['model']
        rental_point_edit_car.classifications = data['classifications']
        rental_point_edit_car.year = data['year']
        rental_point_edit_car.number_plate = data['number_plate']
        rental_point_edit_car.hourly_rate = data['hourly_rate']
        db.session.commit()
    except:
        raise Exception("Notika kļūda!")
        

def set_new_car(data):
    # try:
    car = Car(
        manufacture = data['manufacture'],
        model= data['model'],
        classifications = data['classifications'],
        year = data['year'],
        from_date = datetime.strptime(data['from_date'] + " " + data['from_time'], "%Y-%m-%d %H:%M"),
        to_date = datetime.strptime(data['to_date'] + " " + data['to_time'], "%Y-%m-%d %H:%M"),
        number_plate = data['number_plate'],
        hourly_rate = data['hourly_rate'],
        rental_point_id =  RentalPoint.query.filter(RentalPoint.title == data['rental_point']).first().id
    )
    db.session.add(car)
    db.session.commit()
    return car
    # except:
    #     raise Exception("Notika kļūda!")