from flask import Blueprint

products_bp = Blueprint(
    'products',
    __name__,
    template_folder='templates'
)

# 🔥 Імпорти повинні бути ПІСЛЯ створення Blueprint !
from . import views
