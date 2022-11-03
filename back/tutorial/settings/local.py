from .base import *

DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
    "drf_spectacular",
    "django_extensions",
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://0.0.0.0:3000",
]

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "localhost"]


CORS_ALLOW_HEADERS = (
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "csrftoken",
    "x-requested-with",
    "access-control-allow-origin",
)


MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# REST_FRAMEWORK  += {
# }