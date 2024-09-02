from flask import Blueprint
from .order_controller import get_orders, create_order_controller, update_order_controller, delete_order_controller

order_routes = Blueprint('order_routes', __name__)

order_routes.route('/orders', methods=['GET'])(get_orders)
order_routes.route('/orders', methods=['POST'])(create_order_controller)
order_routes.route('/orders/<int:order_id>', methods=['PUT'])(update_order_controller)
order_routes.route('/orders/<int:order_id>', methods=['DELETE'])(delete_order_controller)
