MESSAGES = {
    'SUCCESS': {
        'USER': {
            'GET': "Success to fetch user",
            'POST': "User created successfully",
            'DELETE': "Success to delete user",
            'UPDATE': "Success to update user"
        },
        'ORDER': {
            'GET': "Success to fetch order",
            'POST': "Order created successfully",
            'DELETE': "Success to delete order",
            'UPDATE': "Success to update order"
        },
        'COSTUMER': {
            'GET': "Success to fetch costumer",
            'POST': "Costumer created successfully",
            'DELETE': "Success to delete costumer",
            'UPDATE': "Success to update costumer"
        },
    },
    'ERROR': {
        'NOT_FOUND': {
            'COSTUMER': "Costumer not found",
            'USER': "User not found",
        },
        'ALREADY': {
            'EMAIL': "Email already exist",
        },
        'INVALID': {
            'EMAIL': "Email is invalid",
            'LOGIN': "Login failed, User not found",
            'PASSWORD_LENGTH': "Password must be at least 8 characters"
        },
        'UNAUTHORIZED': {
            'AUTH': "If you are not logged in, please log in first",
            'FORBIDDEN': "You are not Authorized",
            'EXPIRED': "Token Expired, please log in again",
            'RECOGNIZED': "Token not recognized",
            'ADMIN': "Admin can't access this app",
            "TOKEN_EXPIRED": "Token has expired. Please log in again.",
            "INVALID_TOKEN": "Invalid token. Please log in again."
        },
        'REQUIRED': {
            'EMAIL': "Email is required",
            'PASSWORD': "Password is required",
            'NAME': "Name is required",
            "ITEM_NAME": "Item Name is required",
            "IMAGE": "Image is required",
            "COSTUMER": "Costumer is required"
        },
        # 'RELATION': {
        #     'ANGKATAN': "Angkatan cannot be deleted because it has a relationship"
        # },
        'SERVER_ERROR': {
            'INTERNAL_SERVER_ERROR': "Internal server error"
        }
    },
    'MISC': {
        'SUCCESS': "Success",
        'NOT_FOUND': "Data not found",
        'INVALID': "Invalid request",
        'FORBIDDEN': "Access forbidden",
        'REQUIRED': "Required field missing"
    }
}
