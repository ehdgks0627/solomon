from django.conf import settings
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, message):
        await super(ChatConsumer, self).websocket_connect(message)
        print("Connected!")
        await self.channel_layer.group_add(self.scope["user"].id, self.channel_name)

    async def websocket_disconnect(self, message):
        await self.channel_layer.group_discard(self.scope["user"].id, self.channel_name)
        await super(ChatConsumer, self).websocket_disconnect(message)

    async def receive_json(self, content):
        command = content.get("command", None)
        if command == "read":
            await self.handle_read(content)
        elif command == "send":
            await self.handle_send(content)

    async def handle_read(self, content):
        # TODO save state in db
        message = content.get("message", "")
        receiver = content.get("receiver")
        command = content.get("command")
        await self.channel_layer.group_send(
            receiver,
            {
                "type": "chat.message",
                "sender": self.scope["user"].id,
                "message": message,
                "command": command
            })
        # TODO message id? or ...
        pass

    async def handle_send(self, content):
        # TODO save message in db
        message = content.get("message", "")
        receiver = content.get("receiver")
        command = content.get("command")
        await self.channel_layer.group_send(
            receiver,
            {
                "type": "chat.message",
                "sender": self.scope["user"].id,
                "message": message,
                "command": command
            })

    async def chat_message(self, event):
        await self.send_json({"sender": event["sender"], "message": event["message"], "command": event["command"]})
