from app.hardcodedata import Other
from app.models import Users
from flask_login import LoginManager, login_manager
from .getweather import *
from .login import *
from .logout import *
from .signup import *
from app.config import app

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return Users.query.get(userid)

@login_manager.unauthorized_handler
def ask_to_login():
    return {'Caution!!!': Other.error}
