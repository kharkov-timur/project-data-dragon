from copy import deepcopy
from datetime import timedelta


class Note:
    def __init__(self, title, description, tags = []):
        self.title = title
        self.description = description
        self.tags = tags
        self.created = timedelta.today()

    def get_title(self,):
        return self.title 
    
    def get_text(self,):
        return self.description
    
    def get_tags(self,):
        return self.tags
        
    def add_tag(self, tag):
         self.tags.append(tag)
         
    def remove_tag(self, tag):
        index = self.tags(tag)
        if index == -1:
            raise ValueError(f"Tag {tag} not found")
        else:
            self.tags.remove(tag)
               
    def __str__(self):
        tags_list_str = "; ".join(str(p) for p in self.tags)
        tags_str = f"Tags: {tags_list_str}" if len(self.tags)>0 else ""
        return f"Title: {self.title}\nText: {self.description}\n{tags_str}"

    def __repr__(self):
        tags_list_str = "; ".join(str(p) for p in self.tags)
        tags_str = f"Tags: {tags_list_str}" if len(self.tags)>0 else ""
        return f"Title: {self.title}\nText: {self.description}\n{tags_str}"
   
