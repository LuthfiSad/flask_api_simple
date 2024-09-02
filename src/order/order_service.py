from flask import current_app
import os
from .order_repository import OrderRepository
from ..utils.paginate_data import paginate_data
from ..utils.error_validate import error_validate
from ..utils.messages import MESSAGES
from ..utils.handle_response import handle_response
from ..costumer.costumer_repository import CostumerRepository

def validate_order_data(item_name, costumer_id, image_filename):
    if not image_filename:
        return error_validate(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["REQUIRED"]["IMAGE"])

    if not item_name:
        return error_validate(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["REQUIRED"]["ITEM_NAME"])
    
    if not costumer_id:
        return error_validate(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["REQUIRED"]["COSTUMER"])

    try:
        costumer_id = int(costumer_id)
    except ValueError:
        return error_validate(status=400, code="BAD_REQUEST", message="Costumer ID must be a valid number")

    if not CostumerRepository.find_by_id(costumer_id):
        return error_validate(status=400, code="BAD_REQUEST", message="Costumer ID does not exist")

        
  
def get_all_orders(page, per_page, search_term):
    # Fetch all orders from the repository
    orders = OrderRepository.find_all()
    
    # Apply search filtering
    if search_term:
        filtered_orders = [order for order in orders if search_term.lower() in order.item_name.lower() or search_term.lower() in order.item_name.lower()]
    else:
        filtered_orders = orders

    # Apply pagination
    paginated_orders, meta = paginate_data(filtered_orders, page=page, per_page=per_page)

    # Prepare order data
    base_url = "http://127.0.0.1:5000/storage/image/"
    order_data = [{'id': order.id, 'item_name': order.item_name, 'image': f"{base_url}{order.image}"} for order in paginated_orders]


    return handle_response(status=200, code="SUCCESS", message=MESSAGES["SUCCESS"]["ORDER"]["GET"], data=order_data, meta=meta)

def create_order(item_name, costumer_id, image_filename=None):
    print(item_name, costumer_id, image_filename)
    errors = validate_order_data(item_name, costumer_id, image_filename)
    
    if errors:
      return handle_response(
        status=errors["status"],
        code=errors['code'],
        message=errors['message'],
      )
    
    costumer_id = int(costumer_id)
    OrderRepository.add(item_name, costumer_id, image_filename)
    return handle_response(status=201, code="SUCCESS", message=MESSAGES["SUCCESS"]["ORDER"]["POST"])

def update_order(order_id, item_name, costumer_id, image_filename=None):
    order = OrderRepository.find_by_id(order_id)
    if not order:
      return handle_response(status=400, code="NOT_FOUND", message=MESSAGES["ERROR"]["NOT_FOUND"]["ORDER"])
    
    errors = validate_order_data(item_name, costumer_id, image_filename)
    if errors:
      return handle_response(
        status=errors["status"],
        code=errors['code'],
        message=errors['message'],
      )
      
    if order.image and os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], order.image)):
        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], order.image))
    
    order.item_name = item_name
    order.image = image_filename
    OrderRepository.update(order)
    return handle_response(status=200, code="SUCCESS", message=MESSAGES["SUCCESS"]["ORDER"]["UPDATE"])


def delete_order(order_id):
    order = OrderRepository.find_by_id(order_id)
    if not order:
      return handle_response(status=400, code="NOT_FOUND", message=MESSAGES["ERROR"]["NOT_FOUND"]["ORDER"])

    if order.image and os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], order.image)):
        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], order.image))
    OrderRepository.delete(order)
    return handle_response(status=201, code="SUCCESS",message=MESSAGES["SUCCESS"]["ORDER"]["DELETE"])
