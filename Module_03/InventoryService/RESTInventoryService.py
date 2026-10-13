import time
from flask import Flask, request, jsonify

app = Flask(__name__)
delay = False

@app.route("/check", methods=["POST"])
def check():
    if delay:
        time.sleep(3.0)
    data = request.get_json()
    return jsonify({"ok": True}), 200

@app.route("/delay", methods=["POST"])
def set_delay():
    global delay
    delay = not delay
    return jsonify({"delay": delay}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001)