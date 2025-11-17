from .. import db
from datetime import datetime
from sqlalchemy import Enum

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(
        Enum('news', 'publication', 'tech',"life", 'other', name='category_enum'),
        nullable=False,
        default='other'
    )
    is_active = db.Column(db.Boolean, default=True)
    author = db.Column(db.String(20), default='Anonymous')

    def __repr__(self):
        return f'<Post {self.id} {self.title!r}>'











