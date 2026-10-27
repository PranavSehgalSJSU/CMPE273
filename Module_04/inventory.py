import json
from http.server import BaseHTTPRequestHandler, HTTPServer

db = {"apple": 5, "bananna": 4, "cabbage": 0}

class InventoryHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        item = self.path.strip("/").lower()
        print(f"[Inventory] Looking up item: '{item}'")
        is_available = item in db and db[item] > 0
        print(f"[Inventory] Result for '{item}': {is_available}")
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"available": is_available}).encode("utf-8"))

print("Inventory Service running on port 8082...")
HTTPServer(("", 8082), InventoryHandler).serve_forever()