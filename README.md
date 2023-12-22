## DATA-DRAGON project

---
## Personal contact helper

---

The application allows you to create a personalized contact list with the following fields:
* username
* phone number
* date of birth
* email
* address
* notes

---

The added contacts will be saved to the `contacts.bin` file.

Added notes will be saved to the `notes.bin` file.

---
The application has the following functionality:

General commands:
1. `menu` - show menu
2. `exit/close` - exit from program

Contacts commands:
1. `add-contact [name] [phone] [birthday(optional)]` - add new contact
2. `change-contact` - change contact number
3. `remove-contact [name]` - change contact number
4. `find-phone [name]` - show contact phone
5. `all-contacts` - show all contacts
6. `add-birthday [name] [birthday]` - add birthday to contact
7. `find-birthday [name]` - show birthday of contact
8. `birthdays` - show upcoming birthdays
9. `add-email [name] [email]` - add new email
10. `change-email [name] [email]` - change contact email
11. `add-address [name] [address]` - add address for contact
12. `change-address [name] [address]` - change address of contact
13. `add-tag [name] [new_tag]` - add new tag for contact
14. `change-tag [name] [old_tag] [new_tag]` - renew old tag for contact
15. `find-by-tag [tag]` - searches for a contact by tag
16. `remove-tag [name] [tag]` - remove tag from contact

Notes commands:
1. `add-note` - add new note
2. `add-tag-to-note` - add tag to exist note
3. `set-author` - set author to note
4. `all-notes` - show all notes
5. `change-note-title` - change note title
6. `change-note-text` - change note text
7. `find-note` - find note by title
8. `find-notes-by-tag` - find notes by tag
9. `find-notes-by-author` - find notes by author
10. `remove-tag-from-note` - remove tag from exist note
11. `remove-note` - delete exist note

### How to run the application:
1. Clone the repository
2. Open the project in your IDE
3. Create virtual environment `$ python3 -m venv venv`
4. Activate environment `$ source venv/bin/activate`
5. Run command `$ pip3 install -r requirements.txt` in terminal
6. Run command `$ python3 main.py` in terminal
