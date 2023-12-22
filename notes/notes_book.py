from pathlib import Path
import json
from collections import UserDict
from copy import deepcopy
from notes.note import Note


class NotesBook(UserDict):
    def __init__(self, filepath="notes.json"):
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

    def save_notes_to_file(self):
        with open(self.filepath, "w") as f:
            notes_data = [
                {
                    "author": note.author,
                    "title": note.get_title(),
                    "text": note.get_text(),
                    "tags": note.get_tags(),
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
                    )
                    self.data[note.get_title()] = note

    def __deepcopy__(self, memo):
        copy_object = NotesBook()
        memo[id(copy_object)] = copy_object
        copy_object.data = deepcopy(self.data, memo)
        copy_object.filepath = self.filepath
        return copy_object
