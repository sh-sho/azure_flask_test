from flask import Flask, jsonify, request, abort, url_for, render_template
import requests
import json
# import marshmallow as ma
from flask_smorest import Api, Blueprint, abort
from mysql_files import gen_mission


app = Flask(__name__)
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.json.ensure_ascii = False
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

