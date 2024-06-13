# ruff: noqa: E501
from .base import *  # noqa: F403
from .base import DATABASES
from .base import INSTALLED_APPS
from .base import SPECTACULAR_SETTINGS
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])

# DATABASES
# ------------------------------------------------------------------------------
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

# # CACHES
# # ------------------------------------------------------------------------------
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": env("REDIS_URL"),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "IGNORE_EXCEPTIONS": True,
#         },
#     },
# }

# SECURITY
# ------------------------------------------------------------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS",
    default=True,
)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF",
    default=True,
)

# STORAGES
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["storages"]
# AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
# AWS_QUERYSTRING_AUTH = False
# _AWS_EXPIRY = 60 * 60 * 24 * 7
# AWS_S3_OBJECT_PARAMETERS = {
#     "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate",
# }
# AWS_S3_MAX_MEMORY_SIZE = env.int(
#     "DJANGO_AWS_S3_MAX_MEMORY_SIZE",
#     default=100_000_000,  # 100MB
# )
# AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)
# AWS_S3_CUSTOM_DOMAIN = env("DJANGO_AWS_S3_CUSTOM_DOMAIN", default=None)
# aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
# # STATIC & MEDIA
# # ------------------------
# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTIONS": {
#             "location": "media",
#             "file_overwrite": False,
#         },
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTIONS": {
#             "location": "static",
#             "default_acl": "public-read",
#         },
#     },
# }
# MEDIA_URL = f"https://{aws_s3_domain}/media/"
# COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
# STATIC_URL = f"https://{aws_s3_domain}/static/"

# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="ems <noreply@example.com>",
)
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[ems] ",
)

# ADMIN
# ------------------------------------------------------------------------------
# # Django Admin URL regex.
# ADMIN_URL = env("DJANGO_ADMIN_URL")

# # Anymail
# # ------------------------------------------------------------------------------
# INSTALLED_APPS += ["anymail"]
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# ANYMAIL = {}

# # Collectfast
# # ------------------------------------------------------------------------------
# INSTALLED_APPS = ["collectfast", *INSTALLED_APPS]

# # LOGGING
# # ------------------------------------------------------------------------------
# # A sample logging configuration. The only tangible logging
# # performed by this configuration is to send an email to
# # the site admins on every HTTP 500 error when DEBUG=False.
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
#     "formatters": {
#         "verbose": {
#             "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
#         },
#     },
#     "handlers": {
#         "mail_admins": {
#             "level": "ERROR",
#             "filters": ["require_debug_false"],
#             "class": "django.utils.log.AdminEmailHandler",
#         },
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "verbose",
#         },
#     },
#     "root": {"level": "INFO", "handlers": ["console"]},
#     "loggers": {
#         "django.request": {
#             "handlers": ["mail_admins"],
#             "level": "ERROR",
#             "propagate": True,
#         },
#         "django.security.DisallowedHost": {
#             "level": "ERROR",
#             "handlers": ["console", "mail_admins"],
#             "propagate": True,
#         },
#     },
# }

# django-rest-framework
# -------------------------------------------------------------------------------
SPECTACULAR_SETTINGS["SERVERS"] = [
    {"url": "https://example.com", "description": "Production server"},
]

# EMAIL (REMOVE AFTER TESTING ON THE SERVER)
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend",
)
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# STATIC
# ------------------------------------------------------------------------------
STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(APPS_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = str(APPS_DIR / "media")
MEDIA_URL = "/media/"
