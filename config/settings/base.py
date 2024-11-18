import os
import pymysql
from django.utils.translation import gettext_lazy as _

from config import BASE_DIR, env

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ALLOWED_HOSTS:
# https://docs.djangoproject.com/fr/5.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    "home",
    "blog",
    "misc",
    "contact",
    "search",
    "site_settings",
    "project",
    "utils",
    "experience",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {"default": env.db("DATABASE_URL", default="sqlite:///db.sqlite3")}  # type: ignore

if "mysql" in DATABASES["default"]["ENGINE"]:
    pymysql.install_as_MySQLdb()
    DATABASES["default"]["OPTIONS"] = {
        "charset": "utf8mb4",
        "init_command": "SET NAMES 'utf8mb4' COLLATE 'utf8mb4_unicode_ci', sql_mode='STRICT_TRANS_TABLES'",
    }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LOCAL_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

LANGUAGE = [
    ("en", _("English")),
    ("fr", _("Français")),
]

LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

# https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-STORAGES
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # https://docs.djangoproject.com/en/5.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

# Wagtail settings
WAGTAIL_SITE_NAME = "config"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = env("WAGTAILADMIN_BASE_URL")

# https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#user-uploaded-files
WAGTAILDOCS_EXTENSIONS = [
    "pdf",
    "doc",
    "docx",
    "txt",
    "ppt",
    "pptx",
    "xls",
    "xlsx",
    "csv",
    "mp3",
    "mp4",
    "mov",
    "avi",
    "mkv",
    "key",
    "odt",
    "rtf",
    "zip",
]

WAGTAILIMAGES_EXTENSIONS = [
    "gif",
    "jpg",
    "jpeg",
    "png",
    "svg",
    "mp3",
    "mp4",
    "mov",
    "avi",
    "mkv",
]
