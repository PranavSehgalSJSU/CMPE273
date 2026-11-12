import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

# State variable to simulate readiness status
is_ready = True

@app.route('/')
def home():
    pod_name = socket.gethostname()
    return jsonify({
        "message": "Inventory Service is running",
        "podName": pod_name,
        "items": ["Laptop", "Monitor", "Keyboard"]
    }), 200

@app.route('/healthz/readiness')
def readiness_check():
    if is_ready:
        return "READY", 200
    else:
        return "NOT READY", 500

@app.route('/toggle-unready', methods=['POST', 'GET'])
def toggle_unready():
    global is_ready
    is_ready = False
    return f"Pod {socket.gethostname()} marked UNREADY", 200

@app.route('/toggle-ready', methods=['POST', 'GET'])
def toggle_ready():
    global is_ready
    is_ready = True
    return f"Pod {socket.gethostname()} marked READY", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)