from flask import Flask, request

app = Flask(__name__)


class httpResponse:

    # Success codes
    OK_GET = 200
    OK_POST = 201
    OK_DELETE = 204
    OK_STATUS = 200


@app.route("/person", methods=["GET"])
def get_people():
    if request.headers.get("x-api-key") is None:
        return {}, 401
    return {}, httpResponse.OK_GET


@app.route("/person", methods=["POST"])
def post_person():
    if request.headers.get("x-api-key") is None:
        return {}, 401
    return {}, httpResponse.OK_POST


@app.route("/person/<int:id>", methods=["DELETE"])
def delete_person(id):
    if request.headers.get("x-api-key") is None:
        return {}, 401
    return {}, httpResponse.OK_DELETE


@app.route("/status", methods=["GET"])
def get_status():
    return {}, httpResponse.OK_STATUS


if __name__ == "__main__":
    app.run(debug=True)
