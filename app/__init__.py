import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


from .config import config_map




def create_app(config_name: str = None):
    """Application factory.


    :param config_name: 'development' | 'testing' | 'production' (defaults to FLASK_ENV or 'development')
    """
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


    from .posts import posts_bp
    app.register_blueprint(posts_bp)


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404


    return app