from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey' 
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')

    from .products import products as products_blueprint
    app.register_blueprint(products_blueprint, url_prefix='/products')

    return app
