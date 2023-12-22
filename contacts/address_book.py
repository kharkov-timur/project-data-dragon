from rich.console import Console
from rich.table import Table
from pathlib import Path
import json
from collections import UserDict
from datetime import datetime
from copy import deepcopy
from contacts.record import Record
from contacts.fields import Address


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

    def show_contacts_table(self):
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")

        table.add_column("Name", style="dim", width=20)
        table.add_column("Phones", style="dim", width=15)
        table.add_column("Birthday", style="dim", width=10)
        table.add_column("Email", style="dim", width=25)
        table.add_column("Address", style="dim", width=25)
        table.add_column("Tags", style="dim", width=15)

        for name, record in self.records.items():
            phones = ", ".join([phone.value for phone in record.phones])
            birthday = record.birthday.value if record.birthday else "N/A"
            email = record.email if record.email else "N/A"
            address = record.address.value if record.address else "N/A"
            tags = ", ".join(record.tag)

            table.add_row(name, phones, birthday, email, address, tags)

        console.print(table)

    def save_records_to_file(self):
        records_list = []
        for name, record in self.records.items():
            record_data = {
                "name": name,
                "phones": [phone.value for phone in record.phones],
                "birthday": record.birthday.value if record.birthday else None,
                "email": record.email if record.email else None,
                "address": record.address.value if record.address else None,
                "tag": record.tag,
            }
            records_list.append(record_data)

        with open(self.filepath, "w") as f:
            json.dump(records_list, f, indent=4)

    def load_records_from_file(self):
        if Path(self.filepath).is_file():
            with open(self.filepath, "r") as f:
                records_list = json.load(f)
                for record_data in records_list:
                    record = Record(record_data["name"])
                    for phone_number in record_data["phones"]:
                        record.add_phone(record.name, phone_number)
                    if record_data["birthday"]:
                        record.add_birthday(record_data["birthday"])
                    record.email = (
                        record_data["email"] if record_data["email"] else None
                    )
                    record.address = (
                        Address(record_data["address"])
                        if record_data["address"]
                        else None
                    )
                    record.tag = record_data["tag"] if record_data["tag"] else []
                    self.records[record_data["name"]] = record

    def __deepcopy__(self, memo):
        copy_object = AddressBook()
        memo[id(copy_object)] = copy_object
        copy_object.data = deepcopy(self.data, memo)
        return copy_object
