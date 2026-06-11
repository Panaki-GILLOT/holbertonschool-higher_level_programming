from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


@app.route("/data")
def data():
    return jsonify(sorted(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    body = request.get_json()
    if not body or "username" not in body:
        return jsonify({"error": "Username is required"}), 400
    username = body["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 409
    users[username] = {
        "username": username,
        "name": body.get("name", ""),
        "age": body.get("age", 0),
        "city": body.get("city", ""),
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
