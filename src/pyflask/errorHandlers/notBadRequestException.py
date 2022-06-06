def notBadRequestException(exception):
    """
    Check if the exception is a generic exception.
    """
    return type(exception).__name__ != 'BadRequest' and type(exception).__name__ != 'Forbidden'

