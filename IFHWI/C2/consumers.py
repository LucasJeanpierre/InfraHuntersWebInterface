# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import threading
from .serverSocket import init
from . import sharedSocket


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notification", self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Connected to the server."}))
        self.thread = threading.Thread(target=init, args=("127.0.0.1", 12345))
        self.thread.daemon = True
        self.thread.start()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notification", self.channel_name)

    async def send_notification(self, event):
        message = json.loads(event["message"])
        print("message:", message)
        await self.send(text_data=json.dumps(message))

    async def receive(self, text_data):
        print("Received:", json.dumps(text_data))

        try:
            conn = sharedSocket.shared_socket_conn
            print("conn:", conn)
            if conn:
                conn.sendall(text_data.encode())
        
            
        except Exception as e:
            print(e)
            pass
