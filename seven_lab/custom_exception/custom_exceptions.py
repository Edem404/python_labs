class NegativeValueOfArgumentError(Exception):
    """
    :exception: raise when the presented argument is negative value
    """


class WrongTypeOfArgumentError(Exception):
    """
    :exception: raise when the presented argument belongs to the wrong type of argument
    """


class AlreadyMaxAllowableValueError(Exception):
    """
    :exception: raise when the current value is the maximum allowed
    """
