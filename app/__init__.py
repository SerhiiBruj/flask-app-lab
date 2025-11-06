from flask import Flask

def create_app():
    app = Flask(__name__)

    # Імпортуємо основний блупрінт
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Імпортуємо блупрінт користувачів
    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')

    return app
