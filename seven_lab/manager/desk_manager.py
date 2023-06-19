"""
    packages of models in manager.py
"""

from seven_lab.models.abstract_desk import AbstractDesk
from seven_lab.models.computer_desk import ComputerDesk
from seven_lab.models.coffee_table import CoffeeTable
from seven_lab.models.dressing_table import DressingTable
from seven_lab.models.writing_desk import WritingDesk
from seven_lab.manager.set_manager import SetManager
from seven_lab.custom_decorators.log_parameters import log_parameters
from seven_lab.custom_decorators.iter_length import iter_length
from seven_lab.custom_decorators.exception_logger import exception_logger
from seven_lab.custom_exception.custom_exceptions import NegativeValueOfArgumentError
from seven_lab.custom_exception.custom_exceptions import WrongTypeOfArgumentError


class DeskManager:
    """
        create DeskManager class with list of desks with management methods of desks
    """

    def __init__(self):
        self.__list_of_desk = []

    def add_desk(self, desk):
        """
             add new desk to __list_of_desk
            :param desk:
        """
        self.__list_of_desk.append(desk)

    def __len__(self):
        """
        :return: number of desks in __list_of_desk
        """
        return len(self.__list_of_desk)

    def __getitem__(self, index):
        """
        get item of object_desk_manager by id
        :param index:
        :return: object: The element at the specified index.
        """
        return self.__list_of_desk[index]

    def __iter__(self):
        """
        :return: iter: iterator for the __list_of_desk
        """
        return iter(self.__list_of_desk)

    @log_parameters
    @iter_length
    def find_all_with_min_height_greater_than(self, min_height_in_centimeters):
        """
            Find all desks with minimal height greater than the specified value.
            :param min_height_in_centimeters:
            :return List of desks with minimum height greater than the specified value.:
        """
        return list(filter(lambda desk: desk.min_height > min_height_in_centimeters, self.__list_of_desk))

    @exception_logger(NegativeValueOfArgumentError, "console")
    @log_parameters
    def find_all_with_width_more_than(self, width_in_centimeters):
        """
            Find all desks with width more than the specified value.
            :param width_in_centimeters:
            :return List of desks with width more than the specified value.::
        """
        if width_in_centimeters < 0:
            raise NegativeValueOfArgumentError("Negative value of argument")
        return list(filter(lambda desk: desk.width > width_in_centimeters, self.__list_of_desk))

    @log_parameters
    def get_desks_with_index(self):
        """
        :return: list of formatted string with index of element in __list_of_desk and concatenate this index
                 with element by this index
        """
        return [f"{index}: {desk}" for index, desk in enumerate(self.__list_of_desk, 0)]

    @log_parameters
    def execute_move_down(self, centimeters):
        """
        Execute the move_down method on each desk.
        :param centimeters: centimeters need to move down the table
        :return: list of results of method move_down for every desk in __list_of_desks using list comprehension
        """
        return [desk.move_down(centimeters) for desk in self.__list_of_desk]

    @log_parameters
    def combine_desks_and_move_down(self, centimeters):
        """
        Combine each desk with its corresponding move_down method result.
        :param centimeters: centimeters need to move down the table
        :return: List of tuples containing each desk and its corresponding move_down result.
        """
        value = self.execute_move_down(centimeters)
        return list(zip(self.__list_of_desk, value))

    @log_parameters
    def check_conditions(self, condition):
        """
        Check if all or any desk in the manager satisfies the specified condition
        :param condition: this need to use to satisfies some condition of objects
        :return: dict: A dictionary indicating if all or any desk satisfies the condition.
                        The dictionary has 'all' and 'any' keys with corresponding boolean values.
        """
        all_condition = all(condition(desk) for desk in self.__list_of_desk)
        any_condition = any(condition(desk) for desk in self.__list_of_desk)
        return {"all": all_condition, "any": any_condition}


if __name__ == "__main__":
    desk_manager = DeskManager()

    desk_manager.add_desk(WritingDesk(70, 70, 100, 150, 80, 3, True))
    desk_manager.add_desk(WritingDesk(50, 10, 90, 120, 80, 5, False))
    desk_manager.add_desk(ComputerDesk(70, 70, 100, 150, 80, 3, True))
    desk_manager.add_desk(ComputerDesk(50, 10, 100, 120, 80, 5, False))
    desk_manager.add_desk(DressingTable(80, 40, 140, 165, 120, 6, "ellipse"))
    desk_manager.add_desk(DressingTable(60, 90, 135, 145, 110, 4, "circle"))
    desk_manager.add_desk(CoffeeTable(70, 50, 120, 130, 90, 1, 3))
    desk_manager.add_desk(CoffeeTable(50, 50, 80, 100, 80, 1, 5))

    some_list = desk_manager.find_all_with_width_more_than(-1)

    test_object = WritingDesk(70, 70, 140, 150, 80, 3, True)
    test_dict = test_object.dict_of_type(str)

    test_object.adjust_height(10)
