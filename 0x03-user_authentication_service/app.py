#!/usr/bin/env python3
"""App Entry point"""
import flask
from flask import Flask, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Entry point"""
    return flask.jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """Register user method"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return flask.jsonify(
                {"email": "{}".format(email), "message": "user created"})
    except ValueError:
        return flask.jsonify(
                {"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
