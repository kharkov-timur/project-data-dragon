from fields import Name, Phone, Birthday, Address
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

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

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

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def __str__(self):
        phones_str = "; ".join(str(p) for p in self.phones)
        birthday_str = f", Birthday: {self.birthday}" if self.birthday else ""
        email_str = f", Email: {self.email}" if self.email else ""
        address_str = f", Address: {self.address}" if self.address else ""
        tag_from_list = ", ".join(str(t) for t in self.tag)
        tag_str = f", Tags: {tag_from_list} " if self.tag else ""
        return f"Contact name: {self.name.value}, Phones: {phones_str}{birthday_str}{email_str}{address_str}{tag_str}"

    def get_name(self):
        return self.name.value

    def add_address(self, address):
        self.address = Address(address)
        return f"Address added for {self.name.value}."

    def change_address(self, new_address):
        if not self.address:
            return f"Address for {self.name.value} didn't find, first please add address"

        old_address = self.address.value
        self.address.value = new_address
        return f"Address changed for {self.name.value} from address: {old_address} to new_address: {self.address.value}"

    def add_tag(self, new_tag):
        self.tag.append(new_tag)

    def edit_tag(self, old_tag, new_tag):
        if old_tag in self.tag:
            index = self.tag.index(old_tag)
            self.tag[index] = new_tag
        else:
            raise ValueError(f"Tag {old_tag} not found in this contact")

    def remove_tag_from_contact(self, removed_tag):
        if removed_tag in self.tag:
            self.tag.remove(removed_tag)
            print(f"Removed tag: {removed_tag} from contact: {self.name}")
        else:
            raise ValueError(f"Tag '{removed_tag}' not found in this contact.")

    def __deepcopy__(self, memo):
        copy_object = Record()
        memo[id(copy_object)] = copy_object
        copy_object.name = deepcopy(self.name, memo)
        copy_object.phones = deepcopy(self.phones, memo)
        copy_object.birthday = deepcopy(self.birthday, memo)
        copy_object.email = deepcopy(self.email, memo)
        return copy_object
