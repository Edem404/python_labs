class WritingDesk:
    def __init__(self, number_of_drawers=0, has_keyboard_trey=False, max_weight_capacity=0, current_height=0,
                 max_height=0):
        self.__number_of_drawers = number_of_drawers
        self.__has_keyboard_trey = has_keyboard_trey
        self.__max_weight_capacity = max_weight_capacity
        self.__current_height = current_height
        self.__max_height = max_height

    def adjust_height(self, centimeters):
        if self.__current_height + centimeters > self.__max_height:
            return
        self.__current_height += centimeters

    def move_down(self, centimeters):
        if self.__current_height - centimeters < 0:
            return
        self.__current_height -= centimeters

    @staticmethod
    def get_instance():
        return WritingDesk()

    def __str__(self):
        return f"WritingDesk(number_of_drawers={self.__number_of_drawers}, " \
               f"has_keyboard_trey={self.__has_keyboard_trey}, " \
               f"max_weight_capacity={self.__max_weight_capacity}, " \
               f"current_height={self.__current_height}, " \
               f"max_height={self.__max_height})"


if __name__ == "__main__":
    array_of_writing_desks = [
        WritingDesk(3, True, 200, 120, 150),
        WritingDesk(),
        WritingDesk.get_instance(),
        WritingDesk.get_instance(),
    ]

    for writing_desk in array_of_writing_desks:
        print(writing_desk.__str__())

    writing_desk_object = WritingDesk(3, False, 150, 150, 150)
    writing_desk_object.move_down(20)
    print(writing_desk_object.__str__())

    writing_desk_object.adjust_height(20)
    print(writing_desk_object.__str__())
