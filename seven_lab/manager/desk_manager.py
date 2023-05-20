"""
    packages of models in manager.py
"""
from seven_lab.models.computer_desk import ComputerDesk
from seven_lab.models.coffee_table import CoffeeTable
from seven_lab.models.dressing_table import DressingTable
from seven_lab.models.writing_desk import WritingDesk


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

    def find_all_with_min_height_greater_than(self, min_height_in_centimeters):
        """
            Find all desks with minimal height greater than the specified value.
            :param min_height_in_centimeters:
            :return List of desks with minimum height greater than the specified value.:
        """
        return [desk for desk in self.__list_of_desk if desk.width > min_height_in_centimeters]

    def find_all_with_width_more_than(self, width_in_centimeters):
        """
            Find all desks with width more than the specified value.
            :param width_in_centimeters:
            :return List of desks with width more than the specified value.::
        """
        return [desk for desk in self.__list_of_desk if desk.width > width_in_centimeters]


if __name__ == "__main__":
    desk_manager = DeskManager()

    desk_manager.add_desk(WritingDesk(70, 70, 100, 150, 80, 3, True))
    desk_manager.add_desk(WritingDesk(50, 10, 90, 120, 80, 5, False))
    desk_manager.add_desk(ComputerDesk(70, 70, 100, 150, 80, 3, True))
    desk_manager.add_desk(ComputerDesk(50, 10, 90, 120, 80, 5, False))
    desk_manager.add_desk(DressingTable(80, 40, 140, 165, 120, 6, "ellipse"))
    desk_manager.add_desk(DressingTable(60, 90, 135, 145, 110, 4, "circle"))
    desk_manager.add_desk(CoffeeTable(70, 50, 120, 130, 90, 0, 3))
    desk_manager.add_desk(CoffeeTable(50, 50, 80, 100, 80, 0, 5))

    desks_with_width_more_than = desk_manager.find_all_with_width_more_than(60)

    for i in desks_with_width_more_than:
        print(i)
