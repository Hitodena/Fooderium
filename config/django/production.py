from config.env import env

from .base import *

DEBUG = env.bool("DJANGO_DEBUG", default=False)  # type: ignore

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])  # type: ignore

DJANGO_EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend")
