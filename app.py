from flask import Flask

app = Flask(__name__)


@app.route("/person", methods=["GET"])
def get_people():
    return {}


@app.route("/person", methods=["POST"])
def post_person():
    return {}


@app.route("/person/<int:id>", methods=["DELETE"])
def delete_person(id):
    return {}


@app.route("/status", methods=["GET"])
def get_status():
    return {}


if __name__ == "__main__":
    app.run(debug=True)
