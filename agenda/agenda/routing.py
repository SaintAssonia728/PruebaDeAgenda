from django.urls import re_path
from lista.consumers import ChatConsumer 

websocket_urlpatterns = [
    # Ruta de WebSocket: ws://yourdomain/ws/chat/
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
]