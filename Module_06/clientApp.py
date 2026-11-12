import time
import requests

SERVICE_URL = "http://inventory-service:5000/"

def run_client():
    print("Starting client loop targeting inventory service...")
    while True:
        try:
            response = requests.get(SERVICE_URL, timeout=3)
            data = response.json()
            print(f"[Client Request] Response from Pod: {data.get('podName')}")
        except Exception as err:
            print(f"[Client Request Failed] Error: {err}")
        time.sleep(2)

if __name__ == "__main__":
    run_client()