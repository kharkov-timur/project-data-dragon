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
from notes_commands import (
    add_note_text,
    show_all_notes,
    remove_note,
    change_note_title,
    change_note_text,
    add_note_tag,
    remove_note_tag,
    find_note_tag,
    add_note_author,
    find_note_author,
    find_note
)
from address_book import AddressBook
from notes_book import NotesBook


MENU = """
MENU:
    # menu - show menu
    # add-contact [name] [phone] [birthday(optional)] - add new contact
    # change-contact [name] [phone] - change contact number
    # remove-contact [name] [position] - change contact number
    # find-phone [name] - show contact phone
    # all-contacts - show all contacts
    # add-birthday [name] [birthday] - add birthday to contact
    # find-birthday [name] - show birthday of contact
    # birthdays - show upcoming birthdays
    # add-email [name] [email] - add new email
    # change-email [name] [email] - change contact email
    # save-contacts - save all contacts
    # load-contacts - load all contacts
    # add-address [name] [address] - add address for contact
    # change-address [name] [address] - change address of contact
    # add-note - add new contact
    # remove-note - delete exist note
    # change-note-title - change note title
    # change-note-text - change note text
    # add-tag-to-note - add tag to exist note
    # remove-tag-from-note - remove tag fom exist note
    # find-notes-by-tag - find tag by tag
    # exit/close - exit from program
"""
MENU = MENU+""" 
    # add-note             - add new note
    # find-note            - find note by title
    # all-notes            - show all notes
    # remove-note          - delete exist note
    # change-note-title    - change note title
    # change-note-text     - change note text
    # add-tag-to-note      - add tag to exist note
    # remove-tag-from-note - remove tag fom exist note
    # find-notes-by-tag    - find tag by tag
    # find-notes-by-author - find tag by author
    # set-author           - set author to note
"""

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def main():
    book = AddressBook()
    notes = NotesBook()
    print("\nWelcome to the PERSONAL CONTACT HELPER!")
    print(MENU)
    tmp = None
    prev_command = None
    input_text = "Enter a command: "

    while True:
        user_input = input(input_text)

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

        elif command == "all-notes":
            print(show_all_notes(notes))

        elif command == "add-note":
            input_text = "Enter note title: "
            prev_command = command
            
        elif command == "find-note":
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
            input_text = "Enter note title to  which you want add tag: "
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
            print(find_note( user_input, notes,))
            tmp = None 
            prev_command = None
            input_text = "Enter a command: " 
            
        elif prev_command == "find-notes-by-tag":   
            print(find_note_tag( user_input, notes,))
            tmp = None 
            prev_command = None
            input_text = "Enter a command: "
            
        elif prev_command == "find-notes-by-author":   
            print(find_note_author( user_input, notes,))
            tmp = None 
            prev_command = None
            input_text = "Enter a command: "

        elif prev_command == "remove-tag-from-note":
            if notes.find(user_input):
                input_text = "Enter tag: "
                tmp = user_input
                prev_command = "remove-tag"
            else:
                print(f"Note with title {user_input} not found ")
                prev_command = None
                input_text = "Enter a command: "

        elif prev_command == "add-tag-to-note":
            if notes.find(user_input):
                input_text = "Enter  tag: "
                tmp = user_input
                prev_command = "add-tag"
            else:
                print(f"Note with title {user_input} not found ")
                prev_command = None
                input_text = "Enter a command: "

        elif prev_command == "remove-note":
            if notes.find(user_input):
                print(remove_note(user_input, notes))
                input_text = "Enter a command: "
            else:
                print(f"Note with title {user_input} not found ")
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
                input_text = "Enter a command: "

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

        elif prev_command == "add-note":
            if notes.find(user_input):
                print(f"Note with title {user_input} is exist")
                prev_command = None
                input_text = "Enter a command: "
            else:
                input_text = "Enter note text: "
                tmp = user_input
                prev_command = "title-added"

        elif prev_command == "title-added":
            print(
                add_note_text(
                    user_input,
                    tmp,
                    notes,
                )
            )
            tmp = None
            prev_command = None
            input_text = "Enter a command: "

        elif prev_command == "add-tag":
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
            
        elif prev_command == "add-tag":
            print(add_note_tag(user_input, tmp, notes, ))
            tmp = None 
            prev_command = None
            input_text = "Enter a command: " 
                      
        elif prev_command == "set_author":
            print(add_note_author(user_input, tmp, notes, ))
            tmp = None 
            prev_command = None
            input_text = "Enter a command: "

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
