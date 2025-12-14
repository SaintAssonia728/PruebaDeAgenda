"""
Django settings for agenda project.
...
"""

from pathlib import Path
import environ
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# Leer variables de entorno desde .env
env = environ.Env(DEBUG=(bool, False))
try:
    # Intentionally attempt to read .env if present; ignore if missing on the server
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
except Exception:
    pass

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='dev-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

# If Render (or another host) provides an external hostname, allow it
render_host = os.environ.get('RENDER_EXTERNAL_HOSTNAME') or os.environ.get('RENDER_SERVICE_ID')
if render_host:
    if render_host not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(render_host)

# If running in production (DEBUG=False) and no hosts provided, allow all to avoid
# immediate DisallowedHost during startup — tighten this for real production.
if not DEBUG and (not ALLOWED_HOSTS or ALLOWED_HOSTS == ['']):
    ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True 
# Application definition

INSTALLED_APPS = [
    # --- CAMBIO IMPORTANTE DE ORDEN (Daphne va antes de staticfiles) ---
    'daphne',
    # -------------------------------------------------------------------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    
    'django.contrib.staticfiles',
    
    "corsheaders",
    'rest_framework',
    'lista',
    'channels',
]

from datetime import timedelta

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',    
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'agenda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'agenda.wsgi.application'


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# --- CONFIGURACIÓN CORREGIDA DE ARCHIVOS ESTÁTICOS ---
# Esto obliga a Django a buscar en la carpeta 'static' de la raíz.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# ----------------------------------------------------

# Static files (deployment)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
WHITENOISE_KEEP_ONLY_HASHED_FILES = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- CONFIGURACIONES PARA CHANNELS/WEBSOCKETS ---

# Define la aplicación ASGI principal
ASGI_APPLICATION = 'agenda.asgi.application'

# Configuración del Channel Layer (In-memory para desarrollo)
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
# --------------------------------------------------------