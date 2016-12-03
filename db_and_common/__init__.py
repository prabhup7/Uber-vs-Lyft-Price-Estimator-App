from flask import Flask  # , jsonify, request, json, Response

# TODO: move to model.py
app = Flask(__name__)
import db_and_common.endpoint_for_ui
