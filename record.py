from fields import Name, Phone, Birthday,Address
from copy import deepcopy


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None 

    def add_phone(self, phone):
        new_phone = Phone(phone)
        if new_phone in self.phones:
            raise ValueError("Phone number already exists in this contact")
        self.phones.append(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def find_phone_index(self, phone):
        for index, p in enumerate(self.phones):
            if p.value == phone:
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

    def __str__(self):
        phones_str = "; ".join(str(p) for p in self.phones)
        birthday_str = f", Birthday: {self.birthday}" if self.birthday else ""
        address_str = f", Address: {self.address}" if self.address else ""
        return f"Contact name: {self.name.value}, Phones: {phones_str}{birthday_str}{address_str}"

    def get_name(self):
        return self.name.value
    
    def add_address(self, address):
        self.address = Address(address)
        return f"Adress added for {self.name.value}."
    
    def change_address(self, new_address):
        if not self.address:
            return f"Address for {self.name.value} didn't find,first please add address"

        old_address = self.address.value
        self.address.value = new_address
        return f'Adress changed for {self.name.value} from address: {old_address} to new_address: {self.address.value}'              
    def __deepcopy__(self, memo):
        copy_object = Record()
        memo[id(copy_object)] = copy_object
        copy_object.name = deepcopy(self.name, memo)
        copy_object.phones = deepcopy(self.phones, memo)
        copy_object.birthday = deepcopy(self.birthday, memo)
        return copy_object
