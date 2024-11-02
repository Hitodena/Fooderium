from config.django.base import *
from config.env import env

EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.dummy.EmailBackend")
