from flask import request, json, Response
from flask_sqlalchemy import SQLAlchemy

from db_and_common import app
from db_and_common.model import location
from location_api import googleMaps

db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def test():
    return "Hello from locationApp, Gurnoor"


# ---------------------------------------------------POST--
@app.route('/v1/locations', methods=['POST'])
def create(arg_body=None):
    body = request.get_json(force=True, silent=True)
    if body == None:
        body = arg_body
    # TODO: clean user inputs
    # @arun: make address field mandatory

    loc = persist(body)

    resp = {
        "id": loc.id,
        "name": loc.name,
        "address": loc.address,
        "coordinate": {
            "latitude": loc.latitude,
            "longitude": loc.longitude
        }
    }
    if loc.zip is not None:
        resp['zip'] = loc.zip

    return Response(response=json.dumps(resp), status=201, mimetype='application/json')


# ---------------------------------------------------GET--
@app.route('/v1/locations/<locationId>', methods=['GET'])
def queryDB(locationId):
    loc = location.query.filter_by(id=locationId).first_or_404()
    resp = {
        "id": loc.id,
        "name": loc.name,
        "address": loc.address,
        "coordinate": {
            "latitude": loc.latitude,
            "longitude": loc.longitude
        }
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


def persist(body):
    name = body['name']
    address = body['address']
    zip = None
    if 'zip' in body:
        zip = body['zip']

    coordinate = None
    if zip is not None:
        coordinate = googleMaps.getCoordinates(address + " &postalCode=" + zip)
    else:
        coordinate = googleMaps.getCoordinates(address)
    print (coordinate)
    lat = str(coordinate['lat'])
    longitude = str(coordinate['lng'])

    if zip is not None:
        loc = location(name, address, zip=zip, latitude=lat, longitude=longitude)
    else:
        loc = location(name, address, latitude=lat, longitude=longitude)

    db.session.add(loc)
    db.session.commit()
    return loc
