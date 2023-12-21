from prompt_toolkit.completion import WordCompleter

autocomplete_commands = [
    "menu",
    "add-contact",
    "change-contact",
    "remove-contact",
    "find-phone",
    "all-contacts",
    "add-birthday",
    "find-birthday",
    "birthdays",
    "add-email",
    "change-email",
    "save-contacts",
    "load-contacts",
    "add-address",
    "change-address",
    "add-tag",
    "change-tag",
    "find-by-tag",
    "remove-tag",
    "exit",
    "close",
]

command_completer = WordCompleter(autocomplete_commands, ignore_case=True)
