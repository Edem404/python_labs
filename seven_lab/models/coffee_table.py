"""
    import abstract class of desk AbstractDesk
"""
from seven_lab.models.abstract_desk import AbstractDesk


class CoffeeTable(AbstractDesk):
    """
        CoffeeTable class inherits AbstractDesk class and have additional field num_of_journals
        and override and implements methods from abstract class
    """
    def __init__(self, width=0, length=0, current_height=0,
                 max_height=0, min_height=0, num_of_drawers=0, num_of_journals=0):
        super().__init__(width, length, current_height, max_height, min_height, num_of_drawers)
        self.material_type_set = {"titanium", "glass"}
        self.num_of_journals = num_of_journals

    def adjust_height(self, centimeters):
        """
            adjust the height of the desk by the specified number of centimeters.
            :param centimeters: param on which methods adjust height of desk
        """
        if self.current_height + centimeters > self.max_height:
            self.current_height = self.max_height

        self.current_height += centimeters

    def move_down(self, centimeters):
        """
            move down the height of the desk by the specified number of centimeters.
            :param centimeters: param on which methods move down our desk
        """
        if self.current_height - centimeters < 0:
            self.current_height = 0

        self.current_height -= centimeters

        return f"height of desk was {self.current_height + centimeters} " \
               f"and after moving down height is {self.current_height}"

    def __str__(self):
        """
            :return return a string representation of desk:
        """
        return f"{super().__str__()}" \
               f"num_of_journals={self.num_of_journals})"
