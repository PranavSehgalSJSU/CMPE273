from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import json

class OrderHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        item = "apple"
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                body = self.rfile.read(content_length)
                data = json.loads(body.decode())
                item = data.get("item", "apple")
        except Exception:
            pass

        print(f"[Order] Processing order for item: '{item}'")

        try:
            req = urllib.request.Request(f"http://localhost:8082/{item}")
            with urllib.request.urlopen(req, timeout=2) as resp:
                data = json.loads(resp.read().decode())
                if not data.get("available"):
                    self.send_response(400)
                    self.send_header("Content-Type", "text/plain")
                    self.end_headers()
                    self.wfile.write(f"Item '{item}' unavailable or out of stock".encode())
                    return
        except Exception as e:
            print(f"[Order] Failed to reach inventory: {e}")
            self.send_response(503)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Inventory service down: {str(e)}".encode())
            return
        try:
            urllib.request.urlopen("http://localhost:8083/", data=b"", timeout=2)
        except Exception:
            pass
        
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        response_message = f"order created successfully for : {item}"
        self.wfile.write(response_message.encode())

print("Order Service running on port 8081...")
HTTPServer(("", 8081), OrderHandler).serve_forever()