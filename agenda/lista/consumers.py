import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'global'
        self.room_group_name = f'chat_{self.room_name}'
        
        # Extracción básica del token JWT
        query_string = self.scope['query_string'].decode()
        token = None
        if 'token=' in query_string:
            token = query_string.split('token=')[-1].split('&')[0]
        
        self.user_identifier = token[:8] + '...' if token else 'Anonimo'
        
        if not token:
            await self.close()
            return
            
        await self.accept()
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.send(text_data=json.dumps({
            'message': f'Conectado al Chat Global como {self.user_identifier}.', 
            'user': 'Sistema'
        }))


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')
        
        if not message.strip():
             return

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message', 
                'message': message,
                'user': self.user_identifier
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'user': event['user'],
            'timestamp': datetime.now().strftime('%H:%M:%S')
        }))