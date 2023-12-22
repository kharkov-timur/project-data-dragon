from rich.table import Table
from rich.console import Console


def create_general_menu_table():
    table = Table(title="GENERAL MENU", show_header=True, header_style="bold magenta")
    table.add_column("Command", style="dim", width=12)
    table.add_column("Description", style="dim")

    table.add_row("menu", "Show menu")
    table.add_row("exit/close", "Exit from program")

    return table


def create_contacts_menu_table():
    table = Table(title="CONTACTS MENU", show_header=True, header_style="bold magenta")
    table.add_column("Command", style="dim", width=20)
    table.add_column("Arguments", style="dim")
    table.add_column("Description", style="dim")

    table.add_row("add-contact", "name phone birthday(optional)", "Add a new contact")
    table.add_row("change-contact", "", "Change the phone number")
    table.add_row('remove-contact', 'name', 'Remove contact')
    table.add_row("remove-phone", "", "Remove a phone number")
    table.add_row("find-phone", "name", "Show phone numbers for the specified contact")
    table.add_row("all-contacts", "", "Show all contacts")
    table.add_row("add-birthday", "name birthday", "Add birthday for a contact")
    table.add_row("find-birthday", "name", "Show birthday of a specified contact")
    table.add_row("birthdays", "", "Show upcoming birthdays for the next week")
    table.add_row("add-email", "name email", "Add or update email for a contact")
    table.add_row("change-email", "name email", "Change email of a contact")
    table.add_row("add-address", "name address", "Add an address to a contact")
    table.add_row("change-address", "name address", "Change address of a contact")
    table.add_row("add-tag", "name tag", "Add a new tag to a contact")
    table.add_row("change-tag", "name old_tag new_tag", "Change a tag of a contact")
    table.add_row("find-by-tag", "tag", "Find contacts by a specific tag")
    table.add_row("remove-tag", "name tag", "Remove a tag from a contact")

    return table


def create_notes_menu_table():
    table = Table(title="NOTES MENU", show_header=True, header_style="bold magenta")
    table.add_column("Command", style="dim", width=20)
    table.add_column("Description", style="dim")

    table.add_row("add-note", "Add a new note")
    table.add_row("show-all-notes", "Show all notes")
    table.add_row("remove-note", "Remove a note by title")
    table.add_row("change-note-title", "Change the title of a note")
    table.add_row("change-note-text", "Change the text of a note")
    table.add_row("add-note-tag", "Add a tag to a note")
    table.add_row("find-note", "Find notes by author")
    table.add_row("find-note-by-title", "Find a note by title")
    table.add_row("find-notes-by-tag", "Find notes by tag")
    table.add_row("find-notes-by-author", "Find notes by author")
    table.add_row("remove-tag-from-note", "Remove a tag from a note")

    return table


def menu_table():
    console = Console()
    general_menu = create_general_menu_table()
    contacts_menu = create_contacts_menu_table()
    notes_menu = create_notes_menu_table()

    console.print(general_menu)
    console.print(contacts_menu)
    console.print(notes_menu)
