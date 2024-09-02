import jwt
import datetime
from src.config.index import Envrolment

def encode_token(user_id):
    payload = {
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1),
        'iat': datetime.datetime.now(datetime.timezone.utc),
        'sub': user_id
    }
    return jwt.encode(payload, Envrolment["SECRET_KEY"], algorithm='HS256')

def decode_token(token):
    try:
        print(f"Raw token: {token}")
        payload = jwt.decode(token, Envrolment["SECRET_KEY"], algorithms=['HS256'])
        print("Token decoded successfully")
        return payload['sub']  # Return the user ID or any other info you stored in 'sub'
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        raise jwt.ExpiredSignatureError("Token expired. Please log in again.")
    except jwt.InvalidTokenError:
        print("Invalid token.")
        raise jwt.InvalidTokenError("Invalid token. Please log in again.")
    except Exception as e:
        print(f"Token decoding error: {str(e)}")
        raise Exception(f"Token decoding error: {str(e)}")

