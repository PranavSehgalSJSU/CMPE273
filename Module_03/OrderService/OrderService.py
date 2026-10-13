import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
import httpx
import grpc
import inventory_pb2
import inventory_pb2_grpc

app = Flask(__name__)

@app.route("/order/rest", methods=["POST"])
def order_rest():
    product = request.args.get("product", "apple")
    qty = int(request.args.get("qty", 1))
    try:
        with httpx.Client(timeout=1.0) as client:
            res = client.post(
                "http://127.0.0.1:8001/check",
                json={"product_name": product, "quantity": qty}
            )
            return jsonify({"status": "success", "data": res.json()})
    except Exception as e:
        return jsonify({"status": "timeout_handled", "error": "Timeout"})

@app.route("/order/grpc", methods=["POST"])
def order_grpc():
    product = request.args.get("product", "apple")
    qty = int(request.args.get("qty", 1))
    try:
        with grpc.insecure_channel("127.0.0.1:50051") as channel:
            stub = inventory_pb2_grpc.InventoryServiceStub(channel)
            res = stub.CheckInventory(
                inventory_pb2.OrderRequest(
                    product_name=product,
                    quantity=qty
                ),
                timeout=1.0
            )
            return jsonify({
                "status": "success",
                "data": {"ok": res.ok}
            })
    except grpc.RpcError as e:
        return jsonify({"status": "deadline_handled", "error": "Deadline Exceeded"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)