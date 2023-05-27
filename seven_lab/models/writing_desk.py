"""
    import abstract basic class and abstractmethod decorator
"""
from seven_lab.models.abstract_desk import AbstractDesk


class WritingDesk(AbstractDesk):
    """
        WritingDesk class inherits AbstractDesk class and have additional field has_keyboard_trey
        and override and implements methods from abstract class
        has static private field __instance
    """
    __instance = None

    def __init__(self, width=0, length=0, current_height=0,
                 max_height=0, min_height=0, num_of_drawers=0, has_keyboard_trey=False):
        super().__init__(width, length, current_height, max_height, min_height, num_of_drawers)
        self.material_type_set = {"lypa", "grab"}
        self.has_keyboard_trey = has_keyboard_trey

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
               f"num_of_journals={self.has_keyboard_trey})"

    @staticmethod
    def get_instance():
        """
            method need to return default object
            __instance field assigned once and after this method always will be return __instance
            :return: WritingDesk
        """
        if WritingDesk.__instance is None:
            WritingDesk.__instance = WritingDesk()
        return WritingDesk()
