from flask import Blueprint
from .user_controller import get_users, delete_user_controller

user_routes = Blueprint('user_routes', __name__)

user_routes.route('/users', methods=['GET'])(get_users)
# user_routes.route('/users', methods=['POST'])(create_user_controller)
# user_routes.route('/users/<int:user_id>', methods=['PUT'])(update_user_controller)
user_routes.route('/users/<int:user_id>', methods=['DELETE'])(delete_user_controller)