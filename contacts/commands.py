import re
from prompt_toolkit import prompt
from contacts.record import Record
from custome_output import custom_print
from prompt_toolkit.styles import Style
import builtins

builtins.print = custom_print

style = Style.from_dict({"": "orange", "prompt": "ansipurple"})


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}"

    return wrapper


@input_error
def add_contact(args, book):
    if len(args) not in [2, 3]:
        raise ValueError(
            "Add command expects 2 or 3 arguments: |name| |phone| |birthday| - optional"
        )

    name, phone = args[:2]
    existing_record = book.find(name)

    if existing_record:
        existing_record.add_phone(name, phone)
        book.save_records_to_file()
        return f"Phone number {phone} added to '{name}' contact"
    else:
        record = Record(name)
        record.add_phone(name, phone)

        if len(args) == 3:
            birthday = args[2]
            record.add_birthday(birthday)

        book.add_record(record)
        book.save_records_to_file()
        return "Contact added"


@input_error
def remove_contact(args, book):
    if len(args) != 1:
        raise ValueError("Remove-contact command expects 1 argument: |name|")

    (name,) = args
    record = book.find(name)

    if record:
        book.remove_record(name)
        book.save_records_to_file()
        return f"Contact '{name}' removed"
    else:
        return f"Contact with name '{name}' not found"


@input_error
def change_contact(book):
    name = prompt("Enter the contact name: ", style=style)
    record = book.find(name)

    if not record:
        raise ValueError("Contact not found.")

    phones = record.phones_list()

    if not phones:
        return "No phone numbers available for change"

    print(f"Phone numbers:")
    for idx, phone in enumerate(phones, start=1):
        print(f"{idx}. {phone.value}")

    while True:
        try:
            position = int(
                prompt(
                    "Enter the position of the phone number to change: ", style=style
                )
            )

            if position < 1 or position > len(phones):
                print("Invalid position, please try again")
                continue

            new_phone = prompt("Enter the new phone number: ", style=style)
            record.edit_phone(phones[position - 1].value, new_phone)
            book.save_records_to_file()
            return "Contact updated."
        except ValueError:
            print("Invalid input, please enter a valid number")
        except IndexError:
            print("Invalid position, please try again")


@input_error
def remove_phone(args, book):
    if len(args) != 1:
        raise ValueError("Remove command expects argument |name|")

    name = args[0]
    record = book.find(name)

    if not record:
        return "Contact not found"

    phones = record.phones_list()

    if not phones:
        return "No phone numbers to remove"

    print("Phone numbers:")
    for idx, phone in enumerate(phones, start=1):
        print(f"{idx}. {phone.value}")

    while True:
        try:
            position = prompt(
                "Enter position of phone number to remove (or 'exit/close' to cancel): ",
                style=style,
            )

            if position.lower() in ["exit", "close"]:
                return "Operation canceled."

            position = int(position) - 1

            if position < 0 or position >= len(phones):
                print("Invalid position, please try again")
                continue

            phone_to_remove = phones[position].value
            record.remove_phone(phone_to_remove)
            book.save_records_to_file()
            return f"Phone {phone_to_remove} removed."

        except ValueError:
            print("Please enter a valid number")


@input_error
def find_phone(args, book):
    if len(args) != 1:
        raise ValueError("Phone command expects 1 argument: |name|")

    (name,) = args
    record = book.find(name)

    if record:
        return print(", ".join(phone.value for phone in record.phones))
    else:
        return print("Contact not found")


@input_error
def show_all(book):
    if len(book.records) == 0:
        return print("There are no contacts in the list")
    return book.show_contacts_table()


@input_error
def add_birthday(args, book):
    if len(args) != 2:
        raise ValueError("Add-birthday command expects 2 arguments: |name| |birthday|")
    name, birthday = args
    record = book.find(name)
    if not record:
        raise ValueError("Contact not found")
    record.add_birthday(birthday)
    book.save_records_to_file()
    return "Birthday added"


@input_error
def find_birthday(args, book):
    if len(args) != 1:
        raise ValueError("Show-birthday command expects 1 argument: |name|")

    (name,) = args
    record = book.find(name)

    if record and record.birthday:
        return record.birthday.value
    else:
        return "Birthday not found or contact not found"


@input_error
def birthdays(book):
    birthdays = book.get_birthdays_per_week()
    result = ""

    for day, names in birthdays.items():
        if names:
            result += f"{day}: {', '.join(names)}\n"
    return result if result else "No birthdays in the next week"


@input_error
def add_address(args, book):
    if len(args) < 2:
        raise ValueError("Add-address command expects 2 arguments: |name| |address|")
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    record.add_address(address, book)
    return f"Added address: {address}"


@input_error
def change_address(args, book):
    if len(args) < 2:
        raise ValueError(
            "Change-address command expects 2 arguments: |name| |new address|"
        )

    name = args[0]
    new_address = " ".join(args[1:])
    record = book.find(name)

    if not record:
        raise ValueError("Contact not found")

    old_address = record.address.value if record.address else " Unknown data of address"
    record.add_address(new_address, book)
    book.save_records_to_file()

    return f"Address for {name} updated from {old_address} to {new_address}"


@input_error
def add_tag(args, book):
    if len(args) != 2:
        raise ValueError("Add-tag have to be with 2 argument: |name| |tag|")
    name, tag = args
    record = book.find(name)

    if record is None:
        return f"No contact found with name: {name}"

    record.add_tag(tag, book)
    return f'Added tag: "{tag}" for contact: {name}'


@input_error
def change_tag_by_name(args, book):
    if len(args) != 3:
        raise ValueError(
            "Change-tag command expects 3 arguments: |name| |old_tag| |new_tag|"
        )

    name, old_tag, new_tag = args
    record = book.find(name)

    if record:
        try:
            record.edit_tag(old_tag, new_tag, book)
            return f"Tag changed: {old_tag} -> {new_tag} for contact: {name}"
        except ValueError as e:
            return f"Error: {e}"
    else:
        return f"Contact with name {name} not found"


@input_error
def find_contacts_by_tag(args, book):
    try:
        if len(args) != 1:
            raise ValueError("Find-contacts-by-tag command expects 1 argument: |tag|")

        tag_to_find = args[0]
        matching_contacts = [
            name for name, record in book.records.items() if tag_to_find in record.tags
        ]

        if matching_contacts:
            return book.show_contacts_table(filter_tag=tag_to_find)
        else:
            return print(f"No contacts found with tag '{tag_to_find}'")

    except Exception as e:
        return print(f"Error: {e}")


@input_error
def remove_tag(args, book):
    if len(args) != 2:
        raise ValueError("Remove-tag command expects 2 arguments: |name| |tag|")

    name, removed_tag = args
    record = book.find(name)

    if record:
        if removed_tag in record.tag:
            record.tag.remove(removed_tag)
            book.save_records_to_file()
            return f"Tag: '{removed_tag}' removed from contact: {name}"
        else:
            return f"Tag: '{removed_tag}' not found in contact: {name}"
    else:
        return f"Contact with name {name} not found"


@input_error
def set_email(args, book):
    if len(args) != 2:
        raise ValueError("Current command expects 2 arguments: |name| |email|")
    name, email = args
    if not re.fullmatch(r"^\S+@\S+\.\S+$", email):
        raise ValueError("Please enter valid email")
    record = book.find(name)
    if not record:
        raise ValueError("Contact not found")
    record.set_email(email, book)
    return "Contact updated"
