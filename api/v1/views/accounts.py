#!/usr/bin/python3
""" """
from api.v1.views import app_views
from models import storage
from models.account import Account
from flask import jsonify, abort, request


@app_views.route('/accounts', methods=['GET', 'POST'])
def accounts():
    if request.method == 'GET':
        objs = storage.all(Account)
        return jsonify([account.to_dict() for account in objs])

    if request.method == 'POST':
        account_data = request.get_json()
        if not account_data:
            abort(400, 'Not a JSON')
        if 'vault_id' not in account_data.keys():
            abort(400, 'Vault ID is missing')
        if 'email' not in account_data.keys():
            abort(400, 'Email is missing')
        if 'password_file' not in account_data.keys():
            abort(400, 'Passowrd FILE is missing')
        new_account = Account(**account_data)
        storage.new(new_account)
        storage.save()
        return jsonify(new_account.to_dict()), 201
    #TO REDO POST

@app_views.route('/<vault_id>/accounts', methods=['GET', 'PUT', 'DELETE'])
def account_vault_id(vault_id):
    """ """
    if request.method == 'GET':
        account = storage.get_specific(Account, 'vault_id', vault_id)
        if not account:
            abort(404)
        return jsonify(account.to_dict())
    # TO ADD PUT/DELETE
