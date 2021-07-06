from flask import request
from flask_login import login_user
from flask_restful import Resource
from werkzeug.security import check_password_hash

from app.models import Users
from app.hardcodedata import LoginMessages


class Login(Resource):
    def get(self):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return {'message': LoginMessages.verification_failed}

        user = Users.query.filter_by(email=auth.username).first()

        if not user:
            return {'message': LoginMessages.no_user}

        if check_password_hash(user.password, auth.password):
            login_user(user)
            return {'message': LoginMessages.success}
        else:
            return {'message': LoginMessages.check_password}
