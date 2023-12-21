from prompt_toolkit import prompt
from autocomplete import command_completer
from commands import (
    add_contact,
    change_contact,
    remove_contact,
    find_phone,
    show_all,
    add_birthday,
    find_birthday,
    birthdays,
    save_contacts,
    load_contacts,
    set_email,
    add_address,
    change_address,
)
from address_book import AddressBook


MENU = """
MENU:
    # menu - show menu
    # add-contact - [name] [phone] [birthday(optional)] - add new contact
    # change-contact - [name] [phone] - change contact number
    # remove-contact - [name] [position] - change contact number
    # find-phone - [name] - show contact phone
    # all-contacts - show all contacts
    # add-birthday - [name] [birthday] - add birthday to contact
    # find-birthday - [name] - show birthday of contact
    # birthdays - show upcoming birthdays
    # add-email - [name] [email]  - add new email
    # change-email - [name] [email]  - change contact email
    # save-contacts - save all contacts
    # load-contacts - load all contacts
    # add-address [name] [address] - add address for contact
    # change-address [name] [address] - change address of contact
    # exit/close - exit from program
"""


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def main():
    book = AddressBook()
    print("\nWelcome to the PERSONAL CONTACT HELPER!")
    print(MENU)

    while True:
        user_input = prompt("Enter command: ", completer=command_completer)

        if len(user_input) == 0:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "menu":
            print(MENU)

        elif command == "add-contact":
            print(add_contact(args, book))

        elif command == "change-contact":
            print(change_contact(book))

        elif command == "remove-contact":
            print(remove_contact(args, book))

        elif command == "find-phone":
            print(find_phone(args, book))

        elif command == "all-contacts":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "find-birthday":
            print(find_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))

        elif command == "save-contacts":
            print(save_contacts(book))

        elif command == "load-contacts":
            print(load_contacts(book))

        elif command == "add-email":
            print(set_email(args, book))

        elif command == "change-email":
            print(set_email(args, book))

        elif command == "add-address":
            print(add_address(args, book))

        elif command == "change-address":
            print(change_address(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
