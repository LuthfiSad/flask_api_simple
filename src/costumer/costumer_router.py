from flask import Blueprint
from .costumer_controller import get_costumers, create_costumer_controller, update_costumer_controller, delete_costumer_controller

costumer_routes = Blueprint('costumer_routes', __name__)

costumer_routes.route('/costumers', methods=['GET'])(get_costumers)
costumer_routes.route('/costumers', methods=['POST'])(create_costumer_controller)
costumer_routes.route('/costumers/<int:costumer_id>', methods=['PUT'])(update_costumer_controller)
costumer_routes.route('/costumers/<int:costumer_id>', methods=['DELETE'])(delete_costumer_controller)
