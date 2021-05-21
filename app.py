import os

from logging import debug
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
db_url = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = db_url.replace("://", "ql://", 1) # "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "superSecretAndSecure"
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")

api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)