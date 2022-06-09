from flask import Flask

app = Flask(__name__)


class httpResponse:

    # Success codes
    OK_GET = 200
    OK_POST = 201
    OK_DELETE = 204
    OK_STATUS = 200


@app.route("/person", methods=["GET"])
def get_people():
    return {}, httpResponse.OK_GET


@app.route("/person", methods=["POST"])
def post_person():
    return {}, httpResponse.OK_POST


@app.route("/person/<int:id>", methods=["DELETE"])
def delete_person(id):
    return {}, httpResponse.OK_DELETE


@app.route("/status", methods=["GET"])
def get_status():
    return {}, httpResponse.OK_STATUS


if __name__ == "__main__":
    app.run(debug=True)
