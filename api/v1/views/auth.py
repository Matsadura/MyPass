#!/usr/bin/python3
from api.v1.views import app_views
from models import storage
from models.user import User
from flask import request, jsonify, abort


@app_views.route('/register', methods=['POST'])
def register():
    """ Registers a new user """
    if request.method == 'POST':
        user_info = request.get_json(silent=True)
        if not user_info:
            abort(400, 'Not a JSON')

        required_fields = ['email', 'password', 'first_name', 'last_name']
        missing_fields = [field for field in required_fields if field not in user_info]
        if missing_fields:
            print(missing_fields)
            abort(400, f"{', '.join(missing_fields)} can't be empty")
        existing_user = storage.get_specific(User, 'email', user_info['email'])
        if existing_user:
            abort(400, 'Email already exists')
        new_user = User(**user_info)
        storage.new(new_user)
        storage.save()
        return jsonify(new_user.to_dict()), 201
