import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import grpc
import inventory_pb2
import inventory_pb2_grpc
from concurrent import futures

delay = True#False

class InventoryService(inventory_pb2_grpc.InventoryServiceServicer):
    def CheckInventory(self, request, context):
        if delay:
            time.sleep(3.0)
        return inventory_pb2.OrderResponse(ok=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    inventory_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()