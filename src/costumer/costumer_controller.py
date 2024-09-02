from flask import request
from .costumer_service import create_costumer, update_costumer, delete_costumer, get_all_costumers

def get_costumers():
    # Extract pagination and search parameters from request
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))
    search_term = request.args.get('search', '')

    # Get costumers data from service
    response = get_all_costumers(page, per_page, search_term)

    # Return the paginated and filtered costumer data along with meta information
    return response


def create_costumer_controller():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    response = create_costumer(name, email)
    return response

def update_costumer_controller(costumer_id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    response = update_costumer(costumer_id, name, email)
    
    return response

def delete_costumer_controller(costumer_id):
    response = delete_costumer(costumer_id)
    return response
