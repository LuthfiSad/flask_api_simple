from flask import request
from .user_service import delete_user, get_all_users

def get_users():
    # Extract pagination and search parameters from request
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('perPage', 10))
    search_term = request.args.get('search', '')

    # Get users data from service
    response = get_all_users(page, per_page, search_term)

    # Return the paginated and filtered user data along with meta information
    return response


# def create_user_controller():
#     data = request.json
#     name = data.get('name')
#     email = data.get('email')
    
#     response = create_user(name, email)
#     return response

# def update_user_controller(user_id):
#     data = request.json
#     name = data.get('name')
#     email = data.get('email')
    
#     response = update_user(user_id, name, email)
    
#     return response

def delete_user_controller(user_id):
    response = delete_user(user_id)
    return response
