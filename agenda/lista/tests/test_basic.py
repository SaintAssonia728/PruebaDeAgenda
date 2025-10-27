from django.test import TestCase
from lista.models import Contactos

class ContactoTests(TestCase):
    def test_crear_contacto(self):
        c = Contactos.objects.create(nombre='Prueba', correo='prueba@example.com', telefono='+34123456789')
        self.assertEqual(str(c), 'Prueba')
