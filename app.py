from flask import Flask

app = Flask(__name__)


@app.route("/person", methods=["GET"])
def get_people():
    return {}


@app.route("/person", methods=["POST"])
def post_person():
    return {}, 201


@app.route("/person/<int:id>", methods=["DELETE"])
def delete_person(id):
    return {}, 204


@app.route("/status", methods=["GET"])
def get_status():
    return {}


if __name__ == "__main__":
    app.run(debug=True)
