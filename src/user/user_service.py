from .user_repository import UserRepository
from ..utils.paginate_data import paginate_data
# from ..utils.error_validate import error_validate
from ..utils.messages import MESSAGES
from ..utils.handle_response import handle_response

# def validate_user_data(name, email, id=None):
#     if not name:
#         return error_validate(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["REQUIRED"]["NAME"])
#     if not email:
#         return error_validate(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["REQUIRED"]["EMAIL"])
#     exist = UserRepository.find_by_email(email)
#     if exist and exist.id != id :
#         return error_validate(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["ALREADY"]["EMAIL"])
  
def get_all_users(page, per_page, search_term):
    # Fetch all users from the repository
    users = UserRepository.find_all()
    
    # Apply search filtering
    if search_term:
        filtered_users = [user for user in users if search_term.lower() in user.name.lower() or search_term.lower() in user.email.lower()]
    else:
        filtered_users = users

    # Apply pagination
    paginated_users, meta = paginate_data(filtered_users, page=page, per_page=per_page)

    # Prepare user data
    user_data = [{'id': user.id, 'name': user.name, 'email': user.email, 'password': user.password} for user in paginated_users]

    return handle_response(status=200, code="SUCCESS", message=MESSAGES["SUCCESS"]["USER"]["GET"], data=user_data, meta=meta)

# def create_user(name, email):
#     errors = validate_user_data(name, email)
    
#     if errors:
#       return handle_response(
#         status=errors["status"],
#         code=errors['code'],
#         message=errors['message'],
#       )
      
#     UserRepository.add(name, email)
#     return handle_response(status=201, code="SUCCESS",message=MESSAGES["SUCCESS"]["USER"]["POST"])
    

# def update_user(user_id, name, email):
#     user = UserRepository.find_by_id(user_id)
#     if not user:
#       return handle_response(status=400, code="NOT_FOUND", message=MESSAGES["ERROR"]["NOT_FOUND"]["USER"])
    
#     errors = validate_user_data(name, email, user_id)
#     if errors:
#       return handle_response(
#         status=errors["status"],
#         code=errors['code'],
#         message=errors['message'],
#       )
      
#     user.name = name
#     user.email = email
#     UserRepository.update(user)
#     return handle_response(status=201, code="SUCCESS",message=MESSAGES["SUCCESS"]["USER"]["UPDATE"])

def delete_user(user_id):
    user = UserRepository.find_by_id(user_id)
    if not user:
      return handle_response(status=400, code="NOT_FOUND", message=MESSAGES["ERROR"]["NOT_FOUND"]["USER"])
    UserRepository.delete(user)
    return handle_response(status=201, code="SUCCESS",message=MESSAGES["SUCCESS"]["USER"]["DELETE"])
