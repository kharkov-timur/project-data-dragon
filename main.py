from prompt_toolkit import prompt
from autocomplete import command_completer
from contacts.commands import (
    add_contact,
    change_contact,
    remove_phone,
    find_phone,
    show_all,
    add_birthday,
    find_birthday,
    birthdays,
    set_email,
    add_address,
    change_address,
    add_tag,
    change_tag_by_name,
    find_contacts_by_tag,
    remove_tag,
    remove_contact
)
from notes.notes_commands import (
    add_note_text,
    show_all_notes,
    remove_note,
    remove_note_tag,
    change_note_title,
    change_note_text,
    add_note_tag,
    find_note_tag,
    find_note,
    find_note_by_title,
)
from contacts.address_book import AddressBook
from notes.notes_book import NotesBook
from menu import menu_table


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def main():
    book = AddressBook()
    notes = NotesBook()
    print("\nWelcome to the PERSONAL HELPER!\n")
    menu_table()
    tmp = None
    prev_command = None
    input_text = "Enter a command: "

    while True:
        user_input = prompt(input_text, completer=command_completer)

        if len(user_input) == 0:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "menu":
            menu_table()

        elif command == "add-contact":
            print(add_contact(args, book))
            
        elif command == 'remove-contact':
            print(remove_contact(args, book))
            
        elif command == "change-contact":
            print(change_contact(book))

        elif command == "remove-phone":
            print(remove_phone(args, book))

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

        elif command == "add-email":
            print(set_email(args, book))

        elif command == "change-email":
            print(set_email(args, book))

        elif command == "add-address":
            print(add_address(args, book))

        elif command == "change-address":
            print(change_address(args, book))

        elif command == "add-tag":
            print(add_tag(args, book))

        elif command == "change-tag":
            print(change_tag_by_name(args, book))

        elif command == "find-by-tag":
            print(find_contacts_by_tag(args, book))

        elif command == "remove-tag":
            print(remove_tag(args, book))

        elif command == "all-notes":
            print(show_all_notes(notes))

        elif command == "add-note":
            input_text = "Enter author of the note: "
            prev_command = "author-entered"

        elif command == "find-note":
            input_text = "Enter note author: "
            prev_command = command

        elif command == "find-note-by-title":
            input_text = "Enter note title: "
            prev_command = command

        elif command == "remove-note":
            input_text = "Enter title of note which you want to remove: "
            prev_command = command

        elif command == "change-note-title":
            input_text = "Enter note title in which you want to change title: "
            prev_command = command

        elif command == "change-note-text":
            input_text = "Enter note title in which you want to change text: "
            prev_command = command

        elif command == "add-tag-to-note":
            input_text = "Enter note title to which you want add tag: "
            prev_command = command

        elif command == "remove-tag-from-note":
            input_text = "Enter note title in which you want remove tag: "
            prev_command = command

        elif command == "find-notes-by-tag":
            input_text = "Enter tag: "
            prev_command = command

        elif command == "find-notes-by-author":
            input_text = "Enter author: "
            prev_command = command

        elif command == "set-author":
            input_text = "Enter note title to which you want add author: "
            prev_command = command

        elif prev_command == "set-author":
            if notes.find(user_input):
                input_text = "Enter author: "
                tmp = user_input
                prev_command = "set_author"
            else:
                print(f"Note with title {user_input} not found ")
                prev_command = None
                input_text = "Enter a command: "

        elif prev_command == "find-note":
            print(
                find_note(
                    user_input,
                    notes,
                )
            )
            tmp = None
            prev_command = None
            input_text = "Enter a command: "

        elif prev_command == "find-note-by-title":
            print(
                find_note_by_title(
                    user_input,
                    notes,
                )
            )
            tmp = None
            prev_command = None
            input_text = "Enter a command: "

        elif prev_command == "find-notes-by-tag":
            print(
                find_note_tag(
                    user_input,
                    notes,
                )
            )
            tmp = None
            prev_command = None
            input_text = "Enter a command: "

        elif prev_command == "remove-tag-from-note":
            if notes.find(user_input):
                input_text = "Enter tag: "
                tmp = user_input
                prev_command = "remove-note-tag"
            else:
                print(f"Note with title {user_input} not found ")
                prev_command = None
                input_text = "Enter a command: "

        elif prev_command == "add-tag-to-note":
            if notes.find(user_input):
                input_text = "Enter tag: "
                tmp = user_input
                prev_command = "add-note-tag"
            else:
                print(f"Note with title {user_input} not found ")
                prev_command = None
                input_text = "Enter a command: "

        elif prev_command == "remove-note":
            if notes.find(user_input):
                print(remove_note(user_input, notes))
            else:
                print(f"Note with title {user_input} not found ")
                prev_command = None
                input_text = "Enter a command: "

        elif prev_command == "remove-note-tag":
            print(
                remove_note_tag(
                    user_input,
                    tmp,
                    notes,
                )
            )
            tmp = None
            prev_command = None
            input_text = "Enter a command: "

        elif prev_command == "change-note-title":
            if notes.find(user_input):
                input_text = "Enter new title: "
                tmp = user_input
                prev_command = "change-title"
            else:
                print(f"Note with title {user_input} not found ")
                prev_command = None

        elif prev_command == "change-note-text":
            if notes.find(user_input):
                input_text = "Enter new text: "
                tmp = user_input
                prev_command = "change-text"
            else:
                print(f"Note with title {user_input} not found ")
                prev_command = None
                input_text = "Enter a command: "

        elif prev_command == "change-text":
            print(
                change_note_text(
                    user_input,
                    tmp,
                    notes,
                )
            )
            tmp = None
            prev_command = None
            input_text = "Enter a command: "

        elif prev_command == "change-title":
            print(
                change_note_title(
                    user_input,
                    tmp,
                    notes,
                )
            )
            tmp = None
            prev_command = None
            input_text = "Enter a command: "

        elif prev_command == "author-entered":
            author = user_input
            input_text = "Enter note title: "
            tmp = author
            prev_command = "author-added"

        elif prev_command == "author-added":
            title = user_input
            input_text = "Enter note text: "
            tmp2 = title
            prev_command = "title-added"

        elif prev_command == "title-added":
            text = user_input

            print(
                add_note_text(
                    text,
                    tmp2,
                    tmp,
                    notes,
                )
            )

            tmp = None
            tmp2 = None
            prev_command = None
            input_text = "Enter a command: "

        elif prev_command == "add-note-tag":
            print(
                add_note_tag(
                    user_input,
                    tmp,
                    notes,
                )
            )
            tmp = None
            prev_command = None
            input_text = "Enter a command: "

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
