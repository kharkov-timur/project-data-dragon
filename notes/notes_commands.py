from rich.console import Console
from rich.table import Table
from notes.note import Note
from notes.notes_book import NotesBook


def add_note_text(text: str, title: str, author: str, notes: NotesBook):
    notes.add_record(
        Note(
            title,
            text,
            author,
        )
    )
    return "Note added. You also can add tags to the note using the command add-tag-to-note"


def show_all_notes(notes_book):
    notes = list(notes_book.data.values())
    if not notes:
        return "There are no notes"

    console = Console()

    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("Author")
    table.add_column("Title", style="dim", width=12)
    table.add_column("Description")
    table.add_column("Tags")

    for note in notes:
        tags = ", ".join(note.get_tags()) if note.get_tags() else "No Tags"
        table.add_row(note.author, note.get_title(), note.get_text(), tags)

    console.print(table)


def add_tag_to_note(title: str, tag: str, notes: NotesBook):
    res = notes.find(title)
    if res:
        res.add_tag(tag)
        return f"Tag {tag} added to {title}"


def find_note(author: str, notes: NotesBook):
    res = notes.find(author)
    if not res:
        return f"Note with author {author} not found."
    else:
        return res.__str__()


def find_note_by_title(title: str, notes: NotesBook):
    res = notes.find_by_title(title)
    if not res:
        return f"Note with title {title} not found."
    else:
        return res.__str__()


def remove_note(title: str, notes: NotesBook):
    if not notes.find(title):
        return f"Note with title {title} not found."
    else:
        notes.remove(title)
        return f"Note with title {title} removed"


def change_note_title(new_title: str, old_title: str, notes: NotesBook):
    old_note = notes.find(old_title)
    text = old_note.get_text()
    tags = old_note.get_tags()
    notes.remove(old_title)
    notes.add_record(
        Note(
            new_title,
            text,
            old_note.author,
            tags,
        )
    )
    return f"Title changed from {old_title} to {new_title}"


def change_note_text(title: str, new_text: str, notes: NotesBook):
    old_note = notes.find(title)
    old_text = old_note.get_text()
    tags = old_note.get_tags()
    notes.remove(title)
    notes.add_record(Note(title, new_text, old_note.author, tags))
    return f"Text for {title} changed from {old_text} to {new_text}"


def add_note_tag(tag: str, title: str, notes: NotesBook):
    note = notes.find(title)
    text = note.get_text()
    if tag in note.tags:
        return f"Tag {tag} already added for {title}"
    else:
        note.add_tag(tag)
        notes.remove(title)
        notes.add_record(Note(title, text, note.author, note.tags))
        return f"Tag {tag} added for {title}"


def remove_note_tag(tag: str, title: str, notes: NotesBook):
    old_note = notes.find(title)
    old_text = old_note.get_text()
    tags = old_note.get_tags()
    if tag in tags:
        tags.remove(tag)
        notes.remove(title)
        notes.add_record(Note(title, old_text, old_note.author, tags))
        return f"Tag {tag} added for {title}"
    else:
        return f"No tag {tag} in {title}"


def change_note_author(author: str, title: str, notes: NotesBook):
    note = notes.find(title)
    text = note.get_text()
    tags = note.get_tags()
    notes.add_record(Note(title, text, author, tags))
    return f"Author {author} added for {title}"


def find_note_tag(tag: str, notes: NotesBook):
    res = []
    for i in notes:
        if tag in notes.find(i).get_tags():
            res.append(notes.find(i))
    if len(res) == 0:
        return f"No notes with tag {tag}"
    return res.__str__()


def find_note_author(author: str, notes: NotesBook):
    res = []
    for i in notes:
        if author == notes.find(i).author:
            res.append(notes.find(i))
    if len(res) == 0:
        return f"No notes with author {author}"
    return res.__str__()
