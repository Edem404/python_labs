"""
    import abstract class of desk AbstractDesk
"""
from seven_lab.models.abstract_desk import AbstractDesk


class CoffeeTable(AbstractDesk):
    """
        CoffeeTable class inherits AbstractDesk class and have additional field num_of_journals
        and override and implements methods from abstract class
    """
    def __init__(self, width, length, current_height, max_height, min_height, num_of_drawers, num_of_journals):
        super().__init__(width, length, current_height, max_height, min_height, num_of_drawers)
        self.num_of_journals = num_of_journals

    def adjust_height(self, centimeters):
        """
            adjust the height of the desk by the specified number of centimeters.
            :param centimeters:
        """
        if self.current_height + centimeters > self.max_height:
            self.current_height = self.max_height

        self.current_height += centimeters

    def move_down(self, centimeters):
        """
            move down the height of the desk by the specified number of centimeters.
            :param centimeters:
        """
        if self.current_height - centimeters < 0:
            self.current_height = 0

        self.current_height -= centimeters

    def __str__(self):
        """
            :return return a string representation of desk:
        """
        return f"{super().__str__()}" \
               f"num_of_journals={self.num_of_journals})"
