from app import db
from app.models.models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, email, password, profile_pic=None, bio=None):
    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password=hashed_password, profile_pic=profile_pic, bio=bio)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def create_post(body, user):
    post = Post(body=body, author=user)
    db.session.add(post)
    db.session.commit()
    return post

def get_timeline():
    return Post.query.order_by(Post.timestamp.desc()).limit(5).all()
