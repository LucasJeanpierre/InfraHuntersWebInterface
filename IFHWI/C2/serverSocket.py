import socket
import json
from . import sharedSocket
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



def init(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Number of clients that can wait in the queue

    print("Server is waiting for a connection on ip ", host , " and port ", port)
    conn, addr = server_socket.accept()
    print("Connected by:", addr)

    sharedSocket.shared_socket_conn = conn

    print("shared_socket_conn:", sharedSocket.shared_socket_conn)

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("notification", {"type": "send_notification", "message": json.dumps({'message' : "Connected to " + str(addr)})})

    while True:
        try: 
            data = conn.recv(1024).decode()
            if not data:
                break
            data = json.loads(data)
            print("Received:", data["message"])
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)("notification", {"type": "send_notification", "message": json.dumps({'message' : data["message"]})})

        except KeyboardInterrupt:
            print("Connection aborted.")
            break

    conn.close()