from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"contactos", views.ContactosViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", views.lista_contactos, name="lista_contactos"), # Esta es la ruta principal, que muestra la lista de contactos
    path("contacto/<int:id>/", views.detalle_contactos, name="detalle_contactos"), # Esta ruta muestra el detalle de un contacto, muestra el Nombre, Correo, Telefono y Descripcion
    path("contacto/nuevo/", views.nuevo_contactos, name="nuevo_contactos"), # Esta ruta es para crear un nuevo contacto 
    path("contacto/editar/<int:id>/", views.editar_contactos, name="editar_contactos"), # Esta ruta es para editar un contacto que ya existe
    path("contacto/eliminar/<int:id>/", views.eliminar_contactos, name="eliminar_contactos"), # Esta ruta es para eliminar un contacto que ya existe
    path("buscar/", views.buscar_contactos, name="buscar_contactos"), # Ruta para buscar contactos por nombre
]
# Le cambiamos el nombre a la vista por el que vamos a llamar en este caso Contactos y le damos un nombre a la url para identificarla mejor en la carpeta templates