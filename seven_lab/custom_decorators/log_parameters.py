def log_parameters(func):
    """
    decorator that logs the input arguments and output of a function.
    :param func: function need to decorate
    :return: inner func
    """
    def inner(*args, **kwargs):
        """
        inner function that wraps the original function.
        :param args:
        :param kwargs:
        :return: result of the decorated func
        """
        print(f"input {args, kwargs}")
        result_func = func(*args)
        print(f"output: {result_func}")
        return result_func
    return inner
