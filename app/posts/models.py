from .. import db
from datetime import datetime
from sqlalchemy import Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
post_tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    )


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

    user_id:Mapped[int] = db.Column(db.ForeignKey('users.id'))
    user:Mapped["User"] = db.relationship("User", back_populates="posts")
    tags: Mapped[list["Tag"]] = relationship(secondary=post_tags, back_populates="posts")


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    posts: Mapped[list["Post"]] = db.relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Tag(db.Model):
    __tablename__ = 'tags'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    # Зв'язок "багато до багатьох" з постами
    posts: Mapped[list["Post"]] = relationship(secondary=post_tags, back_populates="tags")






