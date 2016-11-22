from collections import Counter
import logging, requests

logging.basicConfig(level=logging.DEBUG)
from spyne import Application, srpc, ServiceBase, \
    Integer, Unicode
from spyne import Iterable
from spyne.protocol.http import HttpRpc
import json
from spyne.protocol.json import JsonDocument
from spyne.server.wsgi import WsgiApplication
import requests, regex, re
from datetime import datetime, time
from address import AddressParser,Address
import timestring
import timestring


class Determinecrime(ServiceBase):
    @srpc(float, float,float,float,float,_returns=Iterable(Unicode))
    def checkcrime(start_lat,start_lng,end_lat,end_lng,key):
        URL = 'https://api.lyft.com/v1/cost?'
        data = {'start_lat':'37.7772','start_lng':'-122.4233','end_lat':'37.7972','end_lng':'-122.4533','key': 'AIzaSyDuc8IXN9lAoz2pQoT-ES1Q_l1a7U_ryS4'}
        a = requests.get(URL, params=data)
        print a.json()


application = Application([Determinecrime],
                              tns='api.lyft.com',
                              in_protocol=HttpRpc(validator='soft'),
                              out_protocol=JsonDocument()
                         )

app = Application([Determinecrime], tns = 'spyne.examples.hello.http',
        in_protocol=HttpRpc(validator='soft'),
        out_protocol=JsonDocument(),
    )


if __name__ == '__main__':
        # You can use any Wsgi server. Here, we chose
        # Python's built-in wsgi server but you're not
        # supposed to use it in production.
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(app)
    server = make_server('127.0.0.1', 5050, wsgi_app)
    server.serve_forever()