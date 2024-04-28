import os


DEBUG = True
LOG_ROOT = os.environ.get("LOG_ROOT")
LOG_FILENAME = "{}.log".format(os.environ.get("APPLICATION_NAME"))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'encoding': 'utf-8',
            'filename': os.path.join(LOG_ROOT, LOG_FILENAME)
        }
    },
    'loggers': {
        'default': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propogate': True,
        }
    }
}


MONGODB_SETTINGS = {
    'alias': 'default',
    'db': os.environ.get('DB_NAME'),
    'host': os.environ.get('DB_HOST'),
    'port': int(os.environ.get('DB_PORT', 27017)),
    'username': os.environ.get('DB_USERNAME'),
    'password': os.environ.get('DB_PASSWORD'),
}

JWT_SECRET_KEY="qswa6t"

CELERY_SETTINGS = {
    'celery_result_backend': os.environ.get('CELERY_RESULT_BACKEND'),
    'celery_broker_url': os.environ.get('CELERY_BROKER_URL'),
    'allow_empty_password': os.environ.get('ALLOW_EMPTY_PASSWORD'),
    'redis_port': os.environ.get('REDIS_PORT'),
    'redis_host': os.environ.get('REDIS_HOST'),
}