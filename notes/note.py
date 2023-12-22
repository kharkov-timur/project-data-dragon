class Note:
    def __init__(
        self,
        title,
        description,
        author="",
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

    def __str__(self):
        tags_list_str = "; ".join(str(p) for p in self.tags)
        tags_str = f"\nTags: {tags_list_str}" if len(self.tags) > 0 else ""
        author_str = f"\nAuthor: {self.author}" if len(self.author) > 0 else ""
        return (
            f"\n{author_str}\nTitle: {self.title}\nText: {self.description}{tags_str}\n"
        )

    def __repr__(self):
        tags_list_str = "; ".join(str(p) for p in self.tags)
        tags_str = f"\nTags: {tags_list_str}" if len(self.tags) > 0 else ""
        author_str = f"\nAuthor: {self.author}" if len(self.author) > 0 else ""
        return (
            f"\n{author_str}\nTitle: {self.title}\nText: {self.description}{tags_str}\n"
        )
