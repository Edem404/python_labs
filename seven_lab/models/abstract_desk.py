"""
    import abstract basic class and abstractmethod decorator
"""
from abc import ABC, abstractmethod


class AbstractDesk(ABC):
    """
    Abstract base class representing a desk.

    Attributes:
        width : The width of the desk.
        length : The length of the desk.
        current_height : The current height of the desk.
        max_height : The maximum height of the desk.
        min_height : The minimum height of the desk.
        num_of_drawers : The number of drawers in the desk.
        material_type_set : set of types of material of the desk
    """
    def __init__(self, width=0, length=0, current_height=0, max_height=0, min_height=0, num_of_drawers=0):
        self.width = width
        self.length = length
        self.current_height = current_height
        self.max_height = max_height
        self.min_height = min_height
        self.num_of_drawers = num_of_drawers
        self.material_type_set = set()

    @abstractmethod
    def adjust_height(self, centimeters):
        """
            adjust the height of the desk by the specified number of centimeters.
            :param centimeters: param on which methods adjust height of desk
        """

    @abstractmethod
    def move_down(self, centimeters):
        """
            move down the height of the desk by the specified number of centimeters.
            :param centimeters: param on which methods move down our desk
        """

    def get_attributes_by_type(self, data_type):
        """
        get attributes in object by some type
        :param data_type:
        :return:
        """
        return {key: value for key, value in self.__dict__.items()
                if isinstance(value, data_type) and value is not True and value is not False}

    def __str__(self):
        """
            :return return a string representation of desk:
        """
        return f"Desk(width={self.width}, " \
               f"length={self.length}, " \
               f"height={self.current_height}, " \
               f"max_height={self.max_height}, " \
               f"min_height={self.min_height}, " \
               f"num_of_drawers={self.num_of_drawers})"

    def __iter__(self):
        """
        :return: SetManager: iterator object
        """
        return iter(self.material_type_set)

    def __len__(self):
        """
        :return: length of material_type_set
        """
        return len(self.material_type_set)
