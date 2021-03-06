# author : Sam Rapier
from deploy_django_to_azure.settings.base import *

DEBUG = True
INSTALLED_APPS += (
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/staticfiles/'
# STATIC_ROOT = '/staticfiles'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default':{
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'test-DB-exeterOrientation',
        'USER': 'user-admin',
        'PASSWORD': 'v%mRn3os#9P2JnjnV*dJ',
        'PORT': '',
        'HOST': 'db-exeter-orientation.database.windows.net',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'MARS_Connection':'True',
        },

    }
}
