def iter_length(func):
    """
    Decorator that calculates the length of an iterable object returned by a function.
    :param func: func need to decorate
    :return: inner function
    """
    def inner(*args, **kwargs):
        """
        inner function that wraps the original function.
        :param args:
        :param kwargs:
        :return: result of the decorated func
        """
        result_of_func = func(*args, **kwargs)
        if hasattr(result_of_func, '__iter__'):
            length = len(result_of_func)
        else:
            length = 1
        print(f"Length of iterable: {length}")
        return result_of_func

    return inner
