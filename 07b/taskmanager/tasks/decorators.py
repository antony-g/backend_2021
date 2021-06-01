from functools import wraps
from rest_framework.permissions import IsAuthenticated


def define_usage(params=None, returns=None):
    def decorator(function):
        cls = function.view_class
        header = None
        if IsAuthenticated in cls.permission_classes:
            header = {'Authorization': 'Token String'}
        methods = [method.upper() for method in cls.http_method_names if method != 'options']
        usage = {'Request Types': methods, 'Headers': header, 'Body': params, 'Returns': returns}

        @wraps(function)
        def _wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        _wrapper.usage = usage
        return _wrapper
    return decorator
