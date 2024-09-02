from flask import request
from .auth_service import authenticate_user, register_user


def login_controller():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    response = authenticate_user(email, password)
    return response

def register_controller():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    response = register_user(name, email, password)
    return response
