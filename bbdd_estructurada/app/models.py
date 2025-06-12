# app/models.py
from .extensions import db
from datetime import datetime, timezone

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', back_populates='posts')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    posts = db.relationship('Post', back_populates='author')