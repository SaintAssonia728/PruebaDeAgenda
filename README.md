# PruebaDeAgenda - Caso 3

Resumen rápido:
- App Django para gestionar contactos personales con etiquetas (ManyToMany), validaciones, admin personalizado, CRUD, búsqueda y paginación.

Requisitos mínimos para ejecutar (Windows CMD):

1. Crear y activar entorno virtual

```cmd
python -m venv venv
venv\Scripts\activate
```

2. Instalar dependencias

```cmd
pip install -r requirements.txt
```

3. Crear archivo .env a partir de .env.example y ajustar valores

4. Migraciones y superuser

```cmd
cd agenda
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5. Levantar servidor

```cmd
python manage.py runserver
```

6. Probar en navegador
- Admin: http://127.0.0.1:8000/admin/ (crear etiquetas, probar búsqueda, filtro y export CSV)
- App: http://127.0.0.1:8000/ (CRUD, búsqueda, paginación, mensajes)

Despliegue (Heroku/Render/Railway)
- Añadir variables de entorno (SECRET_KEY, DEBUG=False, DATABASE_URL, ALLOWED_HOSTS)
- Asegurar Procfile presente (ya incluido)
- Ejecutar collectstatic durante despliegue

Notas:
- No subir el archivo `.env` al repositorio.
- Si necesitas añadir imágenes/media, configura MEDIA_ROOT y MEDIA_URL en `settings.py`.
