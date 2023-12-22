from pathlib import Path
import json
from collections import UserDict
from datetime import datetime
from copy import deepcopy
from contacts.record import Record


class AddressBook(UserDict):
    WEEK_DAYS_BY_NUMBERS = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    def __init__(self, filepath="contacts.json"):
        super().__init__()
        self.filepath = filepath
        self.records = {}
        self.load_records_from_file()

    def add_record(self, record):
        self.records[record.get_name()] = record
        self.save_records_to_file()

    def remove_record(self, name):
        if name in self.records:
            del self.records[name]
            self.save_records_to_file()

    def find(self, name):
        return self.data.get(name, None)

    def get_birthdays_per_week(self):
        today = datetime.today().date()
        next_week_birthdays_by_weekday = {
            day: [] for day in self.WEEK_DAYS_BY_NUMBERS.values()
        }

        for name, record in self.data.items():
            if record.birthday:
                birthday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if delta_days < 7:
                    birthday_week_day = birthday_this_year.weekday()
                    weekday_name = self.WEEK_DAYS_BY_NUMBERS[birthday_week_day]
                    next_week_birthdays_by_weekday[weekday_name].append(name)

        return next_week_birthdays_by_weekday

    def save_records_to_file(self):
        with open(self.filepath, "w") as f:
            contacts_data = {
                name: {
                    "phones": [phone.value for phone in record.phones],
                    "birthday": record.birthday.value if record.birthday else None,
                    "email": record.email,
                    "address": record.address.value if record.address else None,
                    "tag": record.tag,
                }
                for name, record in self.records.items()
            }
            json.dump(contacts_data, f, indent=4)

    def load_records_from_file(self):
        if Path(self.filepath).is_file():
            with open(self.filepath, "r") as f:
                contacts_data = json.load(f)
                for name, data in contacts_data.items():
                    record = Record(name)
                    self.records[name] = record

    def __deepcopy__(self, memo):
        copy_object = AddressBook()
        memo[id(copy_object)] = copy_object
        copy_object.data = deepcopy(self.data, memo)
        return copy_object
