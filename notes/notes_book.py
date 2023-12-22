from collections import UserDict
from copy import deepcopy


class NotesBook(UserDict):

    def add_record(self, note):
        self.data[note.get_title()] = note

    def find(self, title):
        return self.data.get(title, None)
    
    def find_by_tag(self, tag):
        res = []
        for i in self.data:
            if tag in i.get_tags():
                res.append(i)
        return res.__str__()
    
    def remove(self, title):
            del self.data[title]

    def __deepcopy__(self, memo):
        copy_object = NotesBook()
        memo[id(copy_object)] = copy_object
        copy_object.data = deepcopy(self.data, memo)
        return copy_object
