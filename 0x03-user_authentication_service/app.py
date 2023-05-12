#!/usr/bin/env python3
"""App Entry point"""
import flask
from flask import Flask, request, make_response, abort, url_for
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Login function"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            if session_id is not None:
                resp = flask.jsonify(
                        {"email": "".format(email), "message": "logged in"})
                resp.set_cookie('session_id', session_id)
                return resp
        else:
            abort(401)
    except Exception:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout method"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    else:
        AUTH.destroy_session(user.id)
        return flask.redirect(url_for('hello'))


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """GEt user profile"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    else:
        return flask.jsonify({"email": f"{user.email}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
