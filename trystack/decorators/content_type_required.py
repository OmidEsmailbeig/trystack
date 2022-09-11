from functools import wraps
from flask import request

from trystack.util import jsonify

def content_type_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.content_type != 'application/json':
            return jsonify(
                metadata={
                    'message': 'Content-Type is not supported'
                },
                status=415
            )
        else:
            return func(*args, **kwargs)

    return wrapper
