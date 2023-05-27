"""
file .py in manager python package
"""


class SetManager:
    """
    SetManager class representing a manager for sets in object in object_desk_manager list of objects of Desk
    This class allows iteration over the elements of multiple sets
    """
    def __init__(self, object_desk_manager):
        """
        initialise instance of SetManager
        has field current_object_index with default value 0
        has field current_element_index with default value 0
        :param object_desk_manager: instance of DeskManager
        """
        self.object_desk_manager = object_desk_manager
        self.current_object_index = 0
        self.current_element_index = 0

    def __iter__(self):
        """
        :return: SetManager: iterator object
        """
        return self

    def __len__(self):
        """
        return length, when object_desk_manager has 8 other objects
        and in every of these object have a set or other collection with 2 elements for example
        we got length = 8 * 2 = 16
        :return: int: length of object_desk_manager
        """
        return sum(len(obj.material_type_set) for obj in self.object_desk_manager)

    def __getitem__(self, index):
        """
        get item of object_desk_manager by id
        :param index:
        :return: object: The element at the specified index.
        """
        for obj in self.object_desk_manager:
            if index < len(obj.material_type_set):
                return list(obj.material_type_set)[index]
            index -= len(obj.material_type_set)
        return None

    def __next__(self):
        """
        Returns the next element in the iteration.
        :return: object: The next element.
        :raise: StopIteration: If there are no more elements in the iteration.
        """
        if self.current_object_index >= len(self.object_desk_manager):
            raise StopIteration

        item = self.object_desk_manager[self.current_object_index]
        element = list(item.material_type_set)
        if self.current_element_index >= len(element):
            self.current_object_index += 1
            self.current_element_index = 0
            return self.__next__()

        value = element[self.current_element_index]
        self.current_element_index += 1
        return value
