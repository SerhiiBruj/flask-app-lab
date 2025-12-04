import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from .config import config_map

from sqlalchemy import MetaData
class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
    })

db = SQLAlchemy(model_class=Base)
migrate = Migrate()


def create_app(config_name: str = None):
    """Application factory."""

    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    config_class = config_map.get(config_name, config_map['development'])
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    from app.products.models import Product
    from app.products.models import Category

    from .products import products_bp
    app.register_blueprint(products_bp)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    return app




