"""
URL configuration for agenda project.
...
"""
from django.urls import include, path
from django.contrib import admin

# --- AÑADIR ESTOS IMPORTS ---
from django.conf import settings
from django.conf.urls.static import static
import os
# -----------------------------

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("lista.urls")),  # Añadimos las urls de la app lista
] 

# ------------------------------------------------------------------
# **BLOQUE PARA SERVIR ARCHIVOS ESTÁTICOS EN DESARROLLO**
# Esto es esencial si Django no logra encontrar la carpeta 'static'
# automáticamente y corrige el error 404 para /static/chat.html
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=os.path.join(settings.BASE_DIR, 'static')
    )
# ------------------------------------------------------------------