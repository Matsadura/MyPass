#!/usr/bin/python3
""" """
from api.v1.views import app_views
from models import storage
from models.user import User
from flask import jsonify, request, abort


@app_views.route('/users', methods=['GET'])
def users():
    """ """
    if request.method == 'GET':
        users = storage.all(User).values()
        return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>', methods=['DELETE'])
def user_id_delete(user_id):
    """ """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return {}, 200
