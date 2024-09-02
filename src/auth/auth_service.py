from .auth_repository import UserRepository
from ..utils.token import encode_token
from ..utils.error_validate import error_validate
from ..utils.messages import MESSAGES
from ..utils.handle_response import handle_response
import bcrypt
import re

def validate_user_data(email, password):
    if not email:
        return error_validate(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["REQUIRED"]["EMAIL"])
      
    if not password:
        return error_validate(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["REQUIRED"]["PASSWORD"])

def authenticate_user(email, password):
    errors = validate_user_data(email, password)
    if errors:
      return handle_response(
        status=errors["status"],
        code=errors['code'],
        message=errors['message'],
      )
      
    user = UserRepository.find_by_email(email)
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return handle_response(status=200, code="SUCCESS", message=MESSAGES["SUCCESS"]["USER"]["GET"], data={"token": encode_token(user.id)})
    else:
        return handle_response(status=400, code="NOT_FOUND", message=MESSAGES["ERROR"]["INVALID"]["LOGIN"])

def register_user(name, email, password):
    if not name:
        return handle_response(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["REQUIRED"]["NAME"])

    errors = validate_user_data(email, password)
    if errors:
      return handle_response(
        status=errors["status"],
        code=errors['code'],
        message=errors['message'],
      )
    
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return handle_response(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["INVALID"]["EMAIL"])
    
    exist = UserRepository.find_by_email(email)
    if exist:
        return handle_response(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["ALREADY"]["EMAIL"])

    if len(password) < 8:
        return handle_response(status=400, code="BAD_REQUEST", message=MESSAGES["ERROR"]["INVALID"]["PASSWORD_LENGTH"])
      
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    UserRepository.add(name, email, password=hashed_password)
    return handle_response(status=201, code="SUCCESS",message=MESSAGES["SUCCESS"]["USER"]["POST"])
 
    