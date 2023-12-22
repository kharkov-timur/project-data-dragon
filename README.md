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

The added contacts will be saved to the `contacts.json` file.

Added notes will be saved to the `notes.json` file.

---
The application has the following functionality:

General commands:
1. `menu` - show menu

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
17. `exit/close` - exit from program

Notes commands:
1. `add-note [author] [title] [note] [tag]` - add new note
2. `change-note [author] [title] [note] [tag]` - change note
