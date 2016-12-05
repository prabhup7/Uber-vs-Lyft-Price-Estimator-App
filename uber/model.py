from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


USER = 'root'
PASSWORD = 'root'
DATABASE = 'lab273'
HOSTNAME = 'localhost'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost/location'
db = SQLAlchemy(app)


class location(db.Model):
    __tablename__ = 'location'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    address = db.Column('address', db.String(100))
    city = db.Column('city', db.String(100))
    state = db.Column('state', db.String(100))
    zip = db.Column('zip', db.String(100))
    #coordinate = db.Column('coordinate', db.String(100))
    latitude = db.Column('latitude', db.String(100))
    longitude = db.Column('longitude', db.String(100))

    def __init__(self, name, address, city, state, zip,
                 latitude,longitude):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.latitude = latitude
        self.longitude = longitude
        #self.coordinate = coordinate


def createDB():
    #engine = sqlalchemy.create_engine('mysql://root:123@localhost')  # connect to server
    engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME))
    engine.execute("CREATE DATABASE IF NOT EXISTS %s ;" % (DATABASE))  # create db
    engine.execute("USE location;")
    db.create_all()
    db.session.commit()