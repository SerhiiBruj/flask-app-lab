import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# Загальні параметри


class DevelopmentConfig(Config):
    DEBUG = True
    # Якщо DATABASE_URL задано в .env — використовуємо його, інакше sqlite в папці instance
    SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL',
    'sqlite:///' + str(BASE_DIR / 'instance' / 'dev.db')
    )


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL',
    'sqlite:///:memory:'
    )


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL',
    'sqlite:///' + str(BASE_DIR / 'instance' / 'prod.db')
    )


# Зручний словник для вибору конфігурації по імені
config_map = {
'development': DevelopmentConfig,
'testing': TestingConfig,
'production': ProductionConfig,
}