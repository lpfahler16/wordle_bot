# buffed_list.py

class BuffedList(object):
    """A list with added features."""

    # TODO: Add optional args
    def __init__(self, starter_list):
        self.list = starter_list

    def find_all(self, char):
        """Finds all occurences of a string within this list"""
        return [i for i, letter in enumerate(self.list) if letter == char]
