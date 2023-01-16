import requests
from flask import Flask, request, jsonify
from flask_caching import Cache
from models import User
from db import db
from schema import UserSchema, UserEmailSchema, UserEmailSchemaP
from marshmallow import ValidationError
from flask_pydantic import validate
# from flask_pymongo import PyMongo
from mongodb import MyMongo

app = Flask(__name__)
app.config.from_object('config.BaseConfig')  # Set the configuration variables to the flask application
# cache = Cache(app)  # Initialize Cache
user_schema = UserSchema()
useremail_schema = UserEmailSchema()
useremail_schema_multi = UserEmailSchema(many=True)
mongo = MyMongo(app)


# @app.route("/universities")
# @cache.cached(timeout=100, query_string=True)
# def get_universities():
#     API_URL = "http://universities.hipolabs.com/search?country="
#     search = request.args.get('country')
#     r = requests.get(f"{API_URL}{search}")
#     return jsonify(r.json())


@app.route("/universities/user", methods=["POST"])
def new_user():
    data = request.get_json()
    # try:
    #     user_schema.load(data)
    # except ValidationError as err:
    #     return f"{err}"
    # user = User(username=data["username"],password=data["password"],email=data["email"])
    # user.save_to_db()
    # mongo.db.users.insert_one(data)
    # return {
    #     'username' : data['username'],
    #     'password': data['password'],
    #     'email': data['email']
    # }
    print("salam")
    return mongo.save_to_db(data)


@app.route("/universities/userp", methods=["POST"])
@validate()
def new_userp(body: UserEmailSchemaP):
    user = User(username=body.username, password=body.password, email=body.email)
    user.save_to_db()
    return UserEmailSchemaP(
        username=body.username,
        password=body.password,
        email=body.email
    )

@app.route("/universities/user/<string:name>", methods=["GET"])
def get_user(name):
    # users = mongo.db.users.find({'username': name})
    # result = []
    # for user in users:
    #     user.pop('_id')
    #     result.append(user)

    # return result
    # return {  
    #     'username' : data['username'],
    #     'password': data['password'],
    #     'email': data['email']
    # }
    # return mongo.find_all_by_name(name)
    return mongo.find_one_by_name(name)


@app.route("/universities/user/all", methods=["GET"])
def get_all_users():
    # data = User.all_users()
    # return useremail_schema_multi.dump(data)
    return mongo.find_all()

# db.init_app(app)
# with app.app_context():
#     db.create_all()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

