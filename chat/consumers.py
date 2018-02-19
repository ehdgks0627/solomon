from django.conf import settings
from django.utils import timezone
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Chat
from user.models import Account


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, message):
        await super(ChatConsumer, self).websocket_connect(message)
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
        message = content.get('message', '')
        receiver_id = content.get('receiver_id')
        command = content.get('command')
        Chat.objects.filter(owner=Account.objects.get(id=receiver_id),
                            receiver=self.scope['user'],
                            is_read=False,
                            created_at__lte=timezone.now()).update(is_read=True)
        await self.channel_layer.group_send(
            receiver_id,
            {
                'type': 'chat.message',
                'message': message,
                'command': command,
                'sender': self.scope['user'].id,
            })
        pass

    async def handle_send(self, content):
        message = content.get('message', '')
        receiver_id = content.get('receiver_id')
        command = content.get('command')
        chat = Chat(owner=self.scope['user'],
                    receiver=Account.objects.get(id=receiver_id),
                    message=message)
        chat.save()
        await self.channel_layer.group_send(
            receiver_id,
            {
                'type': 'chat.message',
                'message': message,
                'command': command,
                'sender': self.scope['user'].id,
            })

    async def chat_message(self, event):
        await self.send_json(
            {'sender': event['sender'], 'message': event['message'], 'command': event['command']})
