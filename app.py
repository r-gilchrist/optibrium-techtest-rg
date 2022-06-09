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

    # No x-api-token
    NO_TOKEN = 401

    # Alphanumeric
    NOT_ALPHA = 400

    # Duplicate names
    DUPLICATE = 409


def not_authorised(headers):
    '''Returns True if no x-api-token has been provided'''
    return headers.get("x-api-key") is None


@app.route("/person", methods=["GET"])
def get_people():

    # Check authorisation
    if not_authorised(request.headers):
        return {"error": "Authorization required"}, httpResponse.NO_TOKEN

    return {}, httpResponse.OK_GET


@app.route("/person", methods=["POST"])
def post_person():

    # Check authorisation
    if not_authorised(request.headers):
        return {"error": "Unauthorised"}, httpResponse.NO_TOKEN

    # Get name
    name = request.get_json()["name"]

    # Check if name already exists
    if name in database.get_names():
        return {"error": "Name exists"}, httpResponse.DUPLICATE

    # Check user data is alphanumeric
    if not name.isalpha():
        return {"error": "Names must be alphanumeric"}, httpResponse.NOT_ALPHA

    # Add person to database.db
    id = database.add_person(name)

    return {"id": id, "name": name}, httpResponse.OK_POST


@app.route("/person/<int:id>", methods=["DELETE"])
def delete_person(id):

    # Check authorisation
    if not_authorised(request.headers):
        return {"error": "Unauthorised"}, httpResponse.NO_TOKEN

    # Check if id exists
    if id not in database.get_ids():
        return {"error": "Not Found"}, 404

    return {}, httpResponse.OK_DELETE


@app.route("/status", methods=["GET"])
def get_status():
    return {}, httpResponse.OK_STATUS


if __name__ == "__main__":
    app.run(debug=True)
