import socket
import logging
from datetime import datetime
import pickle
import numpy as np

# Load trained model
with open("/Users/dalal/Documents/Master /selctive_ AI/xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

# Set up logging to file
logging.basicConfig(filename='honeypot_ml.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Generate fake features for testing
def extract_features(ip, port):
    features = [0.0] * 77
    features[0] = 9999   # example: long duration
    features[1] = 80000  # example: high packet count
    features[5] = 1      # example: flag set
    return np.array(features).reshape(1, -1)

# Start honeypot server
def start_honeypot(host='0.0.0.0', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[+] Honeypot is running on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        ip, src_port = client_address
        print(f"[!] Connection from {ip}:{src_port}")
        
        features = extract_features(ip, src_port)
        prediction = model.predict(features)[0]

        label = "Attack" if prediction != 0 else "Benign"
        logging.info(f"Connection from {ip}:{src_port} predicted as: {label}")
        print(f"[*] Predicted: {label}")

        client_socket.send(f"Access recorded. Status: {label}".encode())
        client_socket.close()

if __name__ == "__main__":
    start_honeypot()
