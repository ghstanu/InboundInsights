from DjangoTemplate.settings.default import *  # noqa: F401,F403

ALLOWED_HOSTS = ["localhost", "testserver", "127.0.0.1", ".ngrok.io"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "django-test",
        "USER": "django",
        "PASSWORD": "django",
        "HOST": os.environ.get("DB_HOST"),
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
    }
}

SENTRY_ENV = "test_runner"
