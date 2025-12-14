"""
ASGI config for agenda project.
...
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import agenda.routing # Importamos nuestro nuevo archivo de routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agenda.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(), # Maneja el tráfico HTTP normal
    
    # Maneja las conexiones WebSocket
    "websocket": URLRouter(
        agenda.routing.websocket_urlpatterns
    ),
})