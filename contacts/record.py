import json
from contacts.fields import Name, Phone, Birthday, Address
from copy import deepcopy


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None
        self.tag = []

    def add_phone(self, name, phone):
        new_phone = Phone(phone)

        existed_phone = self.find_phone_index(new_phone)

        if existed_phone != -1:
            raise ValueError(f"Phone number {phone} already exists in {name} contact")
        self.phones.append(new_phone)

    def phones_list(self):
        return self.phones

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday, book):
        self.birthday = Birthday(birthday)
        book.save_records_to_file()

    def find_phone_index(self, phone):
        for index, p in enumerate(self.phones):
            if str(p.value).strip() == str(phone).strip():
                return index
        return -1

    def edit_phone(self, old_phone, new_phone):
        index = self.find_phone_index(old_phone)

        if index == -1:
            raise ValueError(f"Phone number {old_phone} not found in this contact")
        self.phones[index] = Phone(new_phone)

    def remove_phone(self, phone):
        index = self.find_phone_index(phone)

        if index == -1:
            raise ValueError(f"Phone number {phone} not found in this contact")
        del self.phones[index]

    def set_email(self, email, book):
        self.email = email
        book.save_records_to_file()
        return f"Email set to '{email}' for {self.name.value}."

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name.value

    def add_address(self, address, book):
        self.address = Address(address)
        book.save_records_to_file()
        return f"Address added for {self.name.value}."

    def add_tag(self, new_tag, book):
        self.tag.append(new_tag)
        book.save_records_to_file()

    def edit_tag(self, old_tag, new_tag, book):
        if old_tag in self.tag:
            index = self.tag.index(old_tag)
            self.tag[index] = new_tag
            book.save_records_to_file()
        else:
            raise ValueError(f"Tag {old_tag} not found in this contact")

    def save_to_file(self, filepath="contacts.json"):
        with open(filepath, "w") as f:
            record_data = {
                "name": self.get_name(),
                "phones": [phone.value for phone in self.phones],
                "birthday": self.birthday.value if self.birthday else None,
                "email": self.get_email(),
                "address": self.address.value if self.address else None,
                "tag": self.tag,
            }
            json.dump(record_data, f, indent=4)

    def load_from_file(self, filepath="contacts.json"):
        with open(filepath, "r") as f:
            record_data = json.load(f)
            self.name = Name(record_data["name"])
            self.phones = [Phone(phone) for phone in record_data["phones"]]
            self.birthday = (
                Birthday(record_data["birthday"]) if record_data["birthday"] else None
            )
            self.email = record_data["email"]
            self.address = (
                Address(record_data["address"]) if record_data["address"] else None
            )
            self.tag = record_data["tag"]

    def __deepcopy__(self, memo):
        copy_object = Record()
        memo[id(copy_object)] = copy_object
        copy_object.name = deepcopy(self.name, memo)
        copy_object.phones = deepcopy(self.phones, memo)
        copy_object.birthday = deepcopy(self.birthday, memo)
        copy_object.email = deepcopy(self.email, memo)
        return copy_object
