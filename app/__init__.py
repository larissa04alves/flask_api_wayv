from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
    db.init_app(app)

    from .routes import bp as routes_bp
    from .webhook import bp as webhook_bp

    app.register_blueprint(routes_bp)
    app.register_blueprint(webhook_bp)

    return app