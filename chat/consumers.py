from django.conf import settings

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def receive_json(self, content):
        command = content.get("command", None)
        self.base_send({"hi": 1})
        if command == "read":
            await self.handle_read(content)
        elif command == "send":
            await self.handle_send(content)
        elif command == "notify":
            await self.handle_notify(content)

    async def handle_read(self, content):
        # TODO
        pass

    async def handle_send(self, content):
        # TODO
        print(content.get("message"))
        await self.send_json({"a": 1})
        pass

    async def handle_notify(self, content):
        # TODO
        pass
