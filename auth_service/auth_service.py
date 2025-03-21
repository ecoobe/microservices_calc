from flask import Flask, request, jsonify

app = Flask(__name__)
users = {"admin": "password"}

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if users.get(data["username"]) == data["password"]:
        return jsonify({"status": "success"})
    return jsonify({"status": "fail"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)