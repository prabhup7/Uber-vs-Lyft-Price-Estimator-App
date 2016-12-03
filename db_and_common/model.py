import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from db_and_common import app

print 'initializing constants'
USER = 'root'
PASSWORD = '123'
HOST = 'localhost'
DATABASE = 'location'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s' % (USER, PASSWORD, HOST, DATABASE)
db = SQLAlchemy(app)


class location(db.Model):
    print "inside location"
    __tablename__ = 'location'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    address = db.Column('address', db.String(100))
    zip = db.Column('zip', db.String(100))
    latitude = db.Column('latitude', db.String(100))
    longitude = db.Column('longitude', db.String(100))

    def __init__(self, name, address, zip=None,
                 latitude=None, longitude=None):
        self.name = name
        self.address = address
        self.zip = zip
        self.latitude = latitude
        self.longitude = longitude


def createDB():
    # url = 'mysql://%s:%s@%s/%s' % (USER, PASSWORD, HOST, DATABASE)
    url = 'mysql://%s:%s@%s' % (USER, PASSWORD, HOST)
    # print "URL: "+url
    engine = sqlalchemy.create_engine(url)  # connect to server
    # print engine
    create_str = "CREATE DATABASE IF NOT EXISTS %s ;" % (DATABASE)
    # print "create_str: "+create_str
    # sleep(2)
    # conn = engine.connect()
    # conn.execute("commit")
    # conn.execute(create_str)  # create db
    # conn.execute("USE location;")
    # conn.close()

    engine.execute(create_str)
    engine.execute("USE location;")

    db.create_all()
    db.session.commit()
