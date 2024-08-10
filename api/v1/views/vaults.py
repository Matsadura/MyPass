#!/usr/bin/python3
""" """
from api.v1.views import app_views
from models import storage
from models.account import Account
from models.vault import Vault
from models.user import User
from flask import jsonify, request, abort


@app_views.route('/vaults', methods=['GET', 'POST'])
def vaults():
    if request.method == 'GET':
        vaults = storage.all(Vault).values()
        return jsonify([vault.to_dict() for vault in vaults])

    if request.method == 'POST':
        vault_data = request.get_json()
        if not vault_data:
            abort(400, 'Not a JSON')
        if 'user_id' not in vault_data.keys():
            abort(400, 'user_id is missing')
        if 'name' not in vault_data.keys():
            abort(400, 'Name is missing')
        user = storage.get_specific(User, 'id', vault_data['user_id'])
        if not user:
            abort(400, "User doesn't exist")
        new_vault = Vault(**vault_data)
        storage.new(new_vault)
        storage.save()
        return jsonify(new_vault.to_dict()), 201


@app_views.route('/vaults/<vault_id>', methods=['GET', 'PUT'])
def vault_id(vault_id):
    if request.method == 'GET':
        obj = storage.get_specific(Vault, 'id', str(vault_id))
        if not obj:
            abort(404, 'Vault does not exist')
        to_dict = obj.to_dict()
        to_dict.update({"Accounts": storage.count_specific(Account, 'vault_id', vault_id)})
        return jsonify(to_dict)
    #TO ADD PUT
