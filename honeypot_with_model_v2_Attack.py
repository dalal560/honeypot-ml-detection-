import socket
import logging
from datetime import datetime
import pickle
import numpy as np

# Load the pre-trained model
with open("/Users/dalal/Documents/Master /selctive_ AI/xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

# Setup logging to save connection details
logging.basicConfig(filename='honeypot_ml.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Mapping model output to attack types (for multi-class prediction)
attack_types = {
    0: "Benign",
    1: "DoS",
    2: "DDoS",
    3: "PortScan",
    4: "Botnet",
    5: "BruteForce",
    6: "Infiltration"
}

# Use real DoS Hulk sample as feature input
def extract_features(ip, port):
    features = [
        6, 1878, 3, 6, 382, 11595, 382, 0, 127.33, 220.55, 4355, 0, 1932.5, 2182.47, 6377529.286, 4792.33,
        234.75, 229.13, 577, 15, 975, 487.5, 265.17, 675, 300, 1780, 356.0, 399.79, 950, 15, 
        0, 0, 0, 0, 104, 200, 1597.44, 3194.89, 0, 4355, 1197.7, 1886.33, 3558249.75,
        0, 0, 0, 1, 0, 0, 0, 0, 2, 1330.78, 127.33, 1932.5, 0, 0, 0, 0, 0, 0,
        3, 382, 6, 11595, 29200, 235, 1, 32, 0.0, 0.0, 0, 0, 0.0, 0.0, 0, 0
    ]
    return np.array(features).reshape(1, -1)

# Start the honeypot server
def start_honeypot(host='0.0.0.0', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[+] Honeypot is running on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        ip, src_port = client_address
        print(f"[!] Connection from {ip}:{src_port}")

        try:
            features = extract_features(ip, src_port)
            prediction = model.predict(features)[0]
            label = attack_types.get(prediction, f"Unknown ({prediction})")
        except Exception as e:
            label = "Error"
            logging.error(f"Error processing connection from {ip}:{src_port}: {e}")

        logging.info(f"Connection from {ip}:{src_port} predicted as: {label}")
        print(f"[*] Predicted: {label}")

        client_socket.send(f"Access recorded. Status: {label}".encode())
        client_socket.close()

if __name__ == "__main__":
    start_honeypot()
