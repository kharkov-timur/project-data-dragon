from prompt_toolkit.completion import WordCompleter

autocomplete_commands = [
    "menu",
    "add-contact",
    "change-contact",
    "remove-phone",
    "find-phone",
    "all-contacts",
    "add-birthday",
    "find-birthday",
    "birthdays",
    "add-email",
    "change-email",
    "add-address",
    "change-address",
    "add-tag",
    "change-tag",
    "find-by-tag",
    "remove-tag",
    "add-note",
    "find-note",
    "find-note-by-title",
    "all-notes",
    "remove-note",
    "change-note-title",
    "change-note-text",
    "add-tag-to-note",
    "remove-tag-from-note",
    "find-notes-by-tag",
    "find-notes-by-author",
    "exit",
    "close",
]

command_completer = WordCompleter(autocomplete_commands, ignore_case=True)
