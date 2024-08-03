#!/usr/bin/python3
""" """
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """ Returns the API status all wrapped in a json object """
    return {"status": "OK"}, 200


@app_views.route('stats')
def stats():
    """ Returns the count of all classes """
    from models.user import User
    from models.account import Account
    from models.vault import Vault
    from models import storage

    return {"Users": storage.count(User),
            "Vaults": storage.count(Vault),
            "Accounts": storage.count(Account)
            }
