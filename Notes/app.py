from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '6d661d909a7881d61ce3baa7c1cb33fe'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from models import User,Note
from main import main
from auth import auth



app.register_blueprint(main)
app.register_blueprint(auth)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define a simple route
# @app.route('/')
# def index():
#     return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
