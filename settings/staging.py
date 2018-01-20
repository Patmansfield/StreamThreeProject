from settings.base import *

DEBUG = False

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_56yH3vaxIwxp9Cuq9XlaeKFL')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_v1z0pl5hTyLDOHdQwFLgJJN9')

# Paypal environment variables
SITE_URL = 'https://news-revolution.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://cd8e2f31.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'pat.mansfield20@gmail.com'

SITE_URL = 'https://news-revolution.herokuapp.com'

DISQUS_WEBSITE_SHORTNAME = 'news-revolution'
SITE_ID = 2

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

