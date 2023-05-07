#!/usr/bin/env python3
"""Session Authentication view"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models.user import User
import os


SESSION_NAME = os.getenv('SESSION_NAME')


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Login route"""
    from api.v1.app import auth
    email = request.form.get('email')
    password = request.form.get('password')

    if (email is None or email == ""):
        return jsonify({"error": "email missing"}), 400
    if (password is None or password == ""):
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if not users or users is []:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password):
            session_id = auth.create_session(user.id)
            json_user = user.to_json(True)
            resp = jsonify(json_user)
            resp.set_cookie(SESSION_NAME, session_id)
            return resp
    return jsonify({"error": "wrong password"}), 401


@app_views.route(
        '/auth_session/logout',
        methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Logour route"""
    from api.v1.app import auth
    dst_sess = auth.destroy_session(request)
    if not dst_sess:
        return False, abort(404)
    return jsonify({}), 200
