from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'sua_secret_key_aqui'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/microblog.db2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'routes.login'

    from app.routes import routes
    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()

    return app
