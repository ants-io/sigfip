from datetime import datetime
from calendar import timegm
from rest_framework_jwt.settings import api_settings


def jwt_payload_handler(user):
    """ Custom payload handler
    Token encrypts the dictionary returned by this function, and can be decoded by rest_framework_jwt.utils.jwt_decode_handler
    """
    return {
        'user_id': str(user.pk),
        'id': user.id,
        'email': user.email,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
    }


def jwt_response_payload_handler(token, user=None, request=None):
    """ Custom response payload handler.

    This function controlls the custom payload after login or token refresh. This data is returned through the web API.
    """
    return {
        'token': token,
        'user': {
            'id': user.id,
            'email': user.email,
            'user_id': str(user.pk),
            'username': user.username,
            'last_name': user.last_name,
            'first_name': user.first_name,
        }
    }