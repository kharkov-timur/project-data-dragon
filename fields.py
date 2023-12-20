from datetime import datetime
from copy import deepcopy
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __deepcopy__(self, memo):
        copy_object = Field()
        memo[id(self)] = copy_object
        copy_object.value = deepcopy(self.value, memo)
        return copy_object


class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            super().__init__(value)
        except ValueError:
            raise ValueError("Wrong date format")


class Name(Field):
    required = True

    def __init__(self, value):
        if len(value) < 3:
            raise ValueError("Name length should be at least 3 symbols")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Phone length should be exactly 10 digit symbols")
        super().__init__(value)
class Address(Field):
    def __init__(self,value):
        super().__init__(value)