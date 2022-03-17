import math
from typing import Tuple


class EventCalendar:
    """
    Class for handling an event calendar
    """
    def __init__(self):
        """
        Construct an event calendar
        """
        self.calendar = []

    def push(self, t: float, f, data):
        """
        Add event to calendar
        :param t: fire time
        :param f: call back function
        :param data: custom callback data
        """
        i = [0, len(self.calendar)]
        while i[0] != i[1]:
            im = math.floor((i[0] + i[1]) / 2)
            if t >= self.calendar[im][0]:
                i[0] = im + 1
            else:
                i[1] = im
        self.calendar.insert(i[0], (t, f, data))

    def pop(self) -> Tuple:
        """
        Get the nearest time event
        :return: fire time, callback function and custom data
        """
        return self.calendar.pop(0)

    def is_empty(self) -> bool:
        """
        Check whether calendar is empty
        :return: True if calendar is empty
        """
        return len(self.calendar) == 0
