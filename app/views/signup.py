from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from app.config import db
from app.models import Users
from app.hardcodedata import SignupMessages


class Signup(Resource):
    def post(self):
        data = request.get_json()

        password = data['password']
        email = data['email']
        name = data['name']

        if (not name) or (not email) or (not password):
            return {'message': SignupMessages.fill_details}

        email_check = Users.query.filter_by(email=email).first()
        hashed_password = generate_password_hash(password, method='sha256')

        if email_check:
            return {'message': SignupMessages.user_exist}
        else:
            new_user = Users(name=name, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return {'message': SignupMessages.success}