from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# 　ロギング設定
LOGGING = {
    "version": 1,  # 1固定
    "disable_existing_loggers": False,

    # ロガーの設定
    "loggers": {
        # Djangoが利用するロガー
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        # quizアプリケーションが利用するロガー
        "quiz1": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
    # ハンドラの設定
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "dev"
        },
    },

    # フォーマッタの設定
    "formatters": {
        "dev": {
            "format": "\t".join([
                "%(asctime)s",
                "[%(levelname)s]",
                "%(pathname)s(line:%(lineno)d)",
                "%(message)s"
            ])
        },
    }
}

STATICFILES_DIR = (
    os.path.join(BASE_DIR, "static"),
)
