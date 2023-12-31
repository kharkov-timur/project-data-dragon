from rich.console import Console
from rich.table import Table
from pathlib import Path
import json

from collections import UserDict
from copy import deepcopy
from notes.note import Note


class NotesBook(UserDict):
    def __init__(self, filepath="storage/notes.json"):
        super().__init__()
        self.filepath = filepath
        self.load_notes_from_file()

    def add_record(self, note):
        self.data[note.get_title()] = note
        self.save_notes_to_file()

    def find(self, author):
        return self.data.get(author, None)

    def find_by_title(self, title):
        return self.data.get(title, None)

    def find_by_tag(self, tag):
        return [note for note in self.data.values() if tag in note.get_tags()]

    def remove(self, title):
        if title in self.data:
            del self.data[title]
            self.save_notes_to_file()

    def show_notes_table(self, filter_tag=None, filter_author=None, filter_title=None):
        console = Console()
        table = Table(title="NOTES", show_header=True, header_style="bold magenta")

        table.add_column("#", style="dim", width=5)
        table.add_column("Author", style="dim", width=12)
        table.add_column("Title", style="dim", width=20)
        table.add_column("Description", style="dim", width=30)
        table.add_column("Tags", style="dim", width=15)
        table.add_column("Created", style="dim")

        for index, note in enumerate(self.data.values(), start=1):
            if filter_tag and filter_tag not in note.get_tags():
                continue
            if filter_author and filter_author != note.author:
                continue
            if filter_title and filter_title != note.get_title():
                continue

            tags = ", ".join(note.get_tags()) if note.get_tags() else "N/A"
            table.add_row(
                str(index),
                note.author,
                note.get_title(),
                note.get_text(),
                tags,
                note.created_at,
            )

        console.print(table)

    def save_notes_to_file(self):
        with open(self.filepath, "w") as f:
            notes_data = [
                {
                    "author": note.author,
                    "title": note.get_title(),
                    "text": note.get_text(),
                    "tags": note.get_tags(),
                    "created_at": note.created_at,
                }
                for note in self.data.values()
            ]
            json.dump(notes_data, f, indent=4)

    def load_notes_from_file(self):
        if Path(self.filepath).is_file():
            with open(self.filepath, "r") as f:
                notes_data = json.load(f)
                for note_data in notes_data:
                    note = Note(
                        title=note_data["title"],
                        description=note_data["text"],
                        author=note_data["author"],
                        tags=note_data["tags"],
                        created_at=note_data["created_at"],
                    )
                    self.data[note.get_title()] = note

    def __deepcopy__(self, memo):
        copy_object = NotesBook()
        memo[id(copy_object)] = copy_object
        copy_object.data = deepcopy(self.data, memo)
        copy_object.filepath = self.filepath
        return copy_object
