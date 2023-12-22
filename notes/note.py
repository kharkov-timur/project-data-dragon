class Note:
    def __init__(
        self,
        title,
        description,
        author,
        tags=[],
    ):
        self.title = title
        self.description = description
        self.tags = tags
        self.author = author

    def get_title(
        self,
    ):
        return self.title

    def get_text(
        self,
    ):
        return self.description

    def get_tags(
        self,
    ):
        return self.tags

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        index = self.tags(tag)
        if index == -1:
            raise ValueError(f"Tag {tag} not found")
        else:
            self.tags.remove(tag)
