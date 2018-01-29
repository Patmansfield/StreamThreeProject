from base import *

DEBUG = True

DISQUS_WEBSITE_SHORTNAME = 'news-revolution'
SITE_ID = 2

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_56yH3vaxIwxp9Cuq9XlaeKFL')

# Paypal environment variables
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'https://cd8e2f31.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'pat.mansfield20@gmail.com'
