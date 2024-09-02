from flask import Blueprint
from .auth_controller import login_controller, register_controller

auth_routes = Blueprint('auth_routes', __name__)

auth_routes.route('/login', methods=['POST'])(login_controller)
auth_routes.route('/register', methods=['POST'])(register_controller)
