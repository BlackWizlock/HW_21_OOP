class BaseError(Exception):
    message = 'Error!'


class NotEnoughSpace(BaseError):
    message = 'Not enough space'


class NotEnoughProduct(BaseError):
    message = 'Not enough product'


class TooManyDifferentProducts(BaseError):
    message = 'Too many different products'


class InvalidRequest(BaseError):
    message = 'Invalid request'


class InvalidStorageName(BaseError):
    message = 'Invalid storage name'


