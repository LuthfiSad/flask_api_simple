from flask import request
from functools import wraps
from ..utils.token import decode_token
from ..utils.handle_response import handle_response
from ..utils.messages import MESSAGES
from ..config.index import Envrolment
import jwt

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return handle_response(401, "UNAUTHORIZED", MESSAGES["ERROR"]["UNAUTHORIZED"]["FORBIDDEN"])

        try:
            # Extract the token from the header (removing 'Bearer ' prefix)
            token = auth_header.split(" ")[1] if len(auth_header.split(" ")) == 2 else None
            if not token:
                return handle_response(401, "UNAUTHORIZED", MESSAGES["ERROR"]["UNAUTHORIZED"]["FORBIDDEN"])
            
            # Decode token using the secret key from environment variables
            user_id = decode_token(token)
        except jwt.ExpiredSignatureError:
            return handle_response(403, "FORBIDDEN", MESSAGES["ERROR"]["UNAUTHORIZED"]["TOKEN_EXPIRED"])
        except jwt.InvalidTokenError:
            return handle_response(403, "FORBIDDEN", MESSAGES["ERROR"]["UNAUTHORIZED"]["INVALID_TOKEN"])
        except Exception as e:
            return handle_response(403, "FORBIDDEN", str(e))

        return f(*args, **kwargs)
    return decorator

