import sqlalchemy
from flask import Flask, request, json, Response
from flask_sqlalchemy import SQLAlchemy

import googleMaps

DATABASE = 'location'
HOST = 'localhost'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost/location'
db = SQLAlchemy(app)


class location(db.Model):
    __tablename__ = 'location'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    address = db.Column('address', db.String(100))
    city = db.Column('city', db.String(100))
    state = db.Column('state', db.String(100))
    zip = db.Column('zip', db.String(100))
    lat = db.Column('lat', db.String(100))
    longitude = db.Column('longitude', db.String(100))

    def __init__(self, name, address, city, state, zip,
                 lat, longitude):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.lat = lat
        self.longitude = longitude


def createDB():
    engine = sqlalchemy.create_engine('mysql://root:123@localhost')  # connect to server
    engine.execute("CREATE DATABASE IF NOT EXISTS %s ;" % (DATABASE))  # create db
    engine.execute("USE location;")
    db.create_all()
    db.session.commit()


# Flask----------------------------------------------

# ---------------------------------------------------POST--

@app.route('/', methods=['GET'])
def test():
    return "Hello from locationApp, Gurnoor"


@app.route('/v1/locations', methods=['POST'])
def create():
    body = request.get_json(force=True, silent=True)
    name = body['name']
    address = body['address']
    city = body['city']
    state = body['state']
    zip = body['zip']

    # TODO use component filtering if zip available
    coordinate = googleMaps.getCoordinates(address + ", " + city + ", " + state + " &postalCode=" + zip)
    print (coordinate)
    lat = str(coordinate['lat'])
    longitude = str(coordinate['lng'])

    loc = location(name, address, city, state, zip, lat=lat, longitude=longitude)
    db.session.add(loc)
    db.session.commit()
    resp = {
        "id": loc.id,
        "name": loc.name,
        "address": loc.address,
        "city": loc.city,
        "state": loc.state,
        "zip": loc.zip,
        "coordinate": {
            "lat": loc.lat,
            "longitude": loc.longitude
        }

    }

    return Response(response=json.dumps(resp), status=201, mimetype='application/json')


# ---------------------------------------------------GET--
@app.route('/v1/locations/<locationId>', methods=['GET'])
def queryDB(locationId):
    loc = location.query.filter_by(id=locationId).first_or_404()
    resp = {
        "id": loc.id,
        "name": loc.name,
        "address": loc.address,
        "city": loc.city,
        "state": loc.state,
        "zip": loc.zip,
        "lat": loc.lat,
        "longitude": loc.longitude
    }
    return Response(response=json.dumps(resp), status=200, mimetype="application/json")


# ---------------------------------------------------PUT--
@app.route('/v1/locations/<string:locationId>', methods=['PUT'])
def handlePut(locationId):
    body = request.get_json(force=True)
    if body != None:
        newName = body['name']
        print newName
        loc = location.query.filter_by(id=locationId).first_or_404()
        loc.coordinate = newName
        db.session.commit()
        return Response(status=202)
    else:
        return Response(status=400)


# ---------------------------------------------------DELETE--
@app.route('/v1/locations/<string:locationId>', methods=['DELETE'])
def handleDelete(locationId):
    loc = location.query.filter_by(id=locationId).first_or_404()
    db.session.delete(loc)
    db.session.commit()
    return Response(status=204)


if __name__ == '__main__':
    createDB()
    app.run(host='0.0.0.0', port=5009)
