#!/usr/bin/python3
""" Starts the Flask web app """
from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
HOST = "0.0.0.0"
PORT = 5000


@app.teardown_appcontext
def teardown_db(exception):
    """ Closes the storage session """
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """ Handles the 404 error """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    if getenv("MYPASS_API_HOST"):
        HOST = getenv("MYPASS_API_HOST")
    if getenv("MYPASS_API_PORT"):
        PORT = getenv("MYPASS_API_PORT")
    app.run(host=HOST, port=PORT, threaded=True, debug=True)
