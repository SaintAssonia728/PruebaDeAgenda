import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime
from urllib.parse import parse_qs # Necesitas esto para parsear el query string correctamente

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'global'
        self.room_group_name = f'chat_{self.room_name}'
        
        # Extracción segura del token JWT desde el query string
        query_params = parse_qs(self.scope['query_string'].decode())
        token = query_params.get('token', [None])[0]
        
        # --- CORRECCIÓN CRUCIAL DE IDENTIFICACIÓN ---
        # Si no hay token, lo definimos como Anonimo y cerramos la conexión
        if not token:
            self.user_identifier = 'Anonimo'
            await self.close()
            return

        # Si hay token, lo usamos como identificador (primeros 8 chars)
        self.user_identifier = token[:8] + '...' 
        # ----------------------------------------------
        
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

        # self.user_identifier YA ESTÁ DISPONIBLE aquí desde connect()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message', 
                'message': message,
                'user': self.user_identifier # <--- Ya está definido
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'user': event['user'],
            'timestamp': datetime.now().strftime('%H:%M:%S')
        }))