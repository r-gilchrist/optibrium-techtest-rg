from flask import Flask, request
import database

database.ensure_tables_are_created()

app = Flask(__name__)


class httpResponse:

    # Success codes
    OK_GET = 200
    OK_POST = 201
    OK_DELETE = 204
    OK_STATUS = 200

    # Failure codes
    NOT_ALPHANUMERIC = 400
    NO_X_API_TOKEN = 401
    ID_NOT_FOUND = 404
    DUPLICATE_NAME = 409
    NO_NAME_KEY = 410
    INACTIVE_DATABASE = 500


def not_authorised(headers):
    '''Returns True if no x-api-token has been provided'''
    return headers.get("x-api-key") is None


@app.route("/person", methods=["GET"])
def get_people():

    if not_authorised(request.headers):
        return {"error": "Authorization required"}, httpResponse.NO_X_API_TOKEN

    database.ensure_tables_are_created()

    names = database.get_names()
    ids = database.get_ids()
    content = {id: {"name": name} for (id, name) in zip(ids, names)}

    return content, httpResponse.OK_GET


@app.route("/person", methods=["POST"])
def post_person():

    if not_authorised(request.headers):
        return {"error": "Unauthorised"}, httpResponse.NO_X_API_TOKEN

    database.ensure_tables_are_created()

    content = request.get_json()
    if "name" not in content.keys():
        return {"error": "'name' is not specified"}, httpResponse.NO_NAME_KEY

    name = content["name"]
    if name in database.get_names():
        return {"error": "Name exists"}, httpResponse.DUPLICATE_NAME

    if not name.isalpha():
        return {"error": "Names must be alphanumeric"}, httpResponse.NOT_ALPHANUMERIC

    id = database.add_person(name)  # Saves person to disk

    return {"id": id, "name": name}, httpResponse.OK_POST


@app.route("/person/<int:id>", methods=["DELETE"])
def delete_person(id):

    if not_authorised(request.headers):
        return {"error": "Unauthorised"}, httpResponse.NO_X_API_TOKEN

    database.ensure_tables_are_created()

    if id not in database.get_ids():
        return {"error": "Not Found"}, httpResponse.ID_NOT_FOUND

    return {}, httpResponse.OK_DELETE


@app.route("/status", methods=["GET"])
def get_status():

    if database.get_db_status() is False:
        return {"error": "Database is not active"}, httpResponse.INACTIVE_DATABASE

    return {"msg": "OK"}, httpResponse.OK_STATUS


if __name__ == "__main__":
    app.run(debug=True)
