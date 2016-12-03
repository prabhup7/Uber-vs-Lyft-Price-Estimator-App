from flask import request
from flask_sqlalchemy import SQLAlchemy

from db_and_common import app

# from db_and_common.__init__ import location


db = SQLAlchemy(app)


@app.route('/ui')
def parse_and_forward():
    """Parses the parameters in query string
    and posts corresponding request(s) to /v1/location (inside location_api.location_app)"""
    i = 0
    while (request.args.get('Location ' + (str(i))) is not None):
        print "Location " + (str(i)) + ": " + request.args.get('Location ' + (str(i)))
        # TODO: post request
        i += 1

    return "Hello from locationApp, Gurnoor<br/> Query: " + request.query_string + \
           "<br/> location 0: " + request.args.get('Location 0')
