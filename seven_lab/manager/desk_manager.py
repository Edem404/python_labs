"""
    packages of models in manager.py
"""

from seven_lab.models.computer_desk import ComputerDesk
from seven_lab.models.coffee_table import CoffeeTable
from seven_lab.models.dressing_table import DressingTable
from seven_lab.models.writing_desk import WritingDesk
from seven_lab.manager.set_manager import SetManager


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
        print("output:")
        return result_func
    return inner


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
            # length = sum(1 for _ in result)
            length = len(result_of_func)
        else:
            length = 1
        print(f"Length of iterable: {length}")
        return result_of_func

    return inner


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

    @log_parameters
    def find_all_with_width_more_than(self, width_in_centimeters):
        """
            Find all desks with width more than the specified value.
            :param width_in_centimeters:
            :return List of desks with width more than the specified value.::
        """
        return list(filter(lambda desk: desk.width > width_in_centimeters, self.__list_of_desk))

    @log_parameters
    def get_desks_with_index(self):
        """
        :return: list of formatted string with index of element in __list_of_desk and concatenate this index
                 with element by this index
        """
        return [f"{index}: {desk}" for index, desk in enumerate(self.__list_of_desk, 1)]

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

    set_manager = SetManager(desk_manager)
    # print(set_manager.__getitem__(0))
    print(set_manager.__len__())
    print("TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST")
    # result = desk_manager.combine_desks_and_move_down(5)
    for i, y in desk_manager.combine_desks_and_move_down(5):
        print(i, y)

    print("TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST")
    writing_desk = WritingDesk(0.0, 1, 0, False, 0, 0, 0)
    dictionary_test = writing_desk.get_attributes_by_type(int)
    print(dictionary_test)

    print("TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST")
    result = desk_manager.check_conditions(lambda desk: desk.current_height <= 0)
    print(result)

    print("TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST")
    new_set_manager = iter(SetManager(desk_manager))

    print(next(new_set_manager))
    print(next(new_set_manager))
    print(next(new_set_manager))
    print(next(new_set_manager))
    print(next(new_set_manager))
    print(next(new_set_manager))
    print(next(new_set_manager))
    print(next(new_set_manager))

    print(3 % 14 + 1)
    print((27 - 3) % 14 + 1)

    print("================================")
    for i in desk_manager.find_all_with_min_height_greater_than(70):
        print(i)
    print("================================")

    # looking_desks = desk_manager.find_all_with_min_height_greater_than(120)
    #
    # for i in looking_desks:
    #     print(i)
