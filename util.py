__author__ = 'Stepiuk'


def notify(observer):
    def decorator(f):
        def wrapper(*args):
            res = f(*args)
            observer()
            return res

        return wrapper

    return decorator
