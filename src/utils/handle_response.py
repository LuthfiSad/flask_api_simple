from flask import jsonify
from .mesage_code import MESSAGE_CODE

def handle_response(status, code, message, data=None, meta=None):
    response = {
        "status": status,
        "code": MESSAGE_CODE[code],
        "message": message,
    }
    if data is not None:
      response["data"] = data
    if meta:
        response['meta'] = meta
    return jsonify(response), code
