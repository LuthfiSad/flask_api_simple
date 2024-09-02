from flask import request, Response
from .order_service import create_order, update_order, delete_order, get_all_orders
from ..middleware.auth_middleware import token_required
from ..utils.upload_image import upload_image

@token_required
def get_orders():
    # Extract pagination and search parameters from request
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))
    search_term = request.args.get('search', '')

    # Get orders data from service
    response = get_all_orders(page, per_page, search_term)

    # Return the paginated and filtered order data along with meta information
    return response


def create_order_controller():
    item_name = request.form.get('item_name')
    costumer_id = request.form.get('costumer_id')
    
    success, image_filename = upload_image()
    
    if not success:  # Check if upload failed
        return image_filename
    
    response = create_order(item_name, costumer_id, image_filename)
    return response


def update_order_controller(order_id):
    item_name = request.form.get('item_name')
    costumer_id = request.form.get('costumer_id')
    image_filename = upload_image()
    
    if isinstance(image_filename, dict):  # Check if response is an error
        return image_filename
    
    response = update_order(order_id, item_name, costumer_id, image_filename)
    return response


def delete_order_controller(order_id):
    response = delete_order(order_id)
    return response
