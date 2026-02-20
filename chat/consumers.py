import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.utils import timezone
from asgiref.sync import sync_to_async
from .models import Message

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):

    # ---------------------------
    # When User Connects
    # ---------------------------
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        self.user = self.scope["user"]

        # Allow only authenticated users
        if self.user.is_anonymous:
            await self.close()
            return

        # ✅ Mark user ONLINE
        await sync_to_async(User.objects.filter(id=self.user.id).update)(
            is_online=True
        )

        # Join chat room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    # ---------------------------
    # When User Disconnects
    # ---------------------------
    async def disconnect(self, close_code):
        if not self.user.is_anonymous:
            # ✅ Mark OFFLINE + update last_seen
            await sync_to_async(User.objects.filter(id=self.user.id).update)(
                is_online=False,
                last_seen=timezone.now()
            )

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # ---------------------------
    # Receive Message from Frontend
    # ---------------------------
    async def receive(self, text_data):
        data = json.loads(text_data)

        # ---------------------------
        # Typing Indicator (no DB save)
        # ---------------------------
        if data.get("typing"):
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "typing_event",
                    "user": self.user.username
                }
            )
            return

        # ---------------------------
        # Normal Message
        # ---------------------------
        message = data.get("message")
        receiver_id = data.get("receiver")

        if not message or message.strip() == "":
            return  # Prevent empty messages

        receiver = await sync_to_async(User.objects.get)(id=receiver_id)

        # ✅ Save message in database
        await sync_to_async(Message.objects.create)(
            sender=self.user,
            receiver=receiver,
            content=message
        )

        # Send to WebSocket group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": self.user.username,
            }
        )

    # ---------------------------
    # Send Chat Message to Clients
    # ---------------------------
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "sender": event["sender"]
        }))

    # ---------------------------
    # Send Typing Event to Clients
    # ---------------------------
    async def typing_event(self, event):
        await self.send(text_data=json.dumps({
            "typing": True,
            "user": event["user"]
        }))
