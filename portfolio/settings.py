from pathlib import Path
import os
# from dotenv import load_dotenv
from decouple import config, Csv
# from .jazzmin_settings import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS
from django.core.management.utils import get_random_secret_key



BASE_DIR = Path(__file__).resolve().parent.parent
# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = 'django-insecure-+oa#*%b@98v6%82=%$8*ibq*xi6bji=)cw)is2^isi8gw&aoi+'

DEBUG=True
# DEBUG=config('DEBUG',default=True,cast=bool)

# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    # 'jazzmin',

    'ckeditor',
    'admin_interface',
    "colorfield",
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


DATABASES = {
    
        
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'db_name',                      
#         'USER': 'db_user',
#         'PASSWORD': 'db_user_password',
#         'HOST': '',
#         'PORT': 'db_port_number',
#     }
}
    


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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# media setting
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# # ckeditor
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # You can customize the toolbar settings as needed.
        'height': 300,         # Set the height of the CKEditor field.
    },
}


# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]




# # Jazzmin settings 
# JAZZMIN_SETTINGS = {
#     "site_title": "Resume Admin",
#     "site_header": "Resume Admin",
#     "site_brand": "Resume Admin",
#     "site_logo": "PortfolioWebsite-Django\static\assets\img\portfolio.png",  # Set your logo path
#     "login_logo": "PortfolioWebsite-Django\static\assets\img\profile-img.jpg",  # Set your logo path
#     "login_logo_dark": None,
#     "site_icon": None,
#     "welcome_sign": "Welcome to the Resume Admin",
#     "copyright": "Resume Admin",
#     # "search_model": ["auth.User", "main.YourModel"],

#     "topmenu_links": [
#         {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
#         {"model": "auth.User"},
#         {"app": "yourapp"},
#     ],

#     "usermenu_links": [
#         {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
#         {"model": "auth.user"}
#     ],

#     "show_sidebar": True,
#     "navigation_expanded": True,
#     "hide_apps": [],
#     "hide_models": [],
#     "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
#     "custom_links": {
#         "books": [{
#             "name": "Make Messages", "url": "make_messages", "icon": "fas fa-comments", "permissions": ["books.view_book"]
#         }]
#     },
#     "icons": {
#         "auth": "fas fa-users-cog",
#         "auth.user": "fas fa-user",
#         "auth.Group": "fas fa-users",
#     },
#     "default_icon_parents": "fas fa-chevron-circle-right",
#     "default_icon_children": "fas fa-circle",
#     "related_modal_active": False,
#     "custom_css": None,
#     "custom_js": None,
#     "show_ui_builder": False,
# }

# JAZZMIN_UI_TWEAKS = {
#     "theme": "cosmo",
#     "dark_mode_theme": None,
# }
# JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
# JAZZMIN_UI_TWEAKS = JAZZMIN_UI_TWEAKS

# Define custom error handlers
handler404 = 'portfolio.views.custom_404'
handler500 = 'portfolio.views.custom_500'