# abstractFactory

from abc import ABC, abstractmethod


class AbcItem(ABC):

    def __init__(self, caption):
        self.caption = caption

    @abstractmethod
    def make_html(self):
        pass


class PageItem(AbcItem):

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = []

    def add(self, item):
        self.content.append(item)

    def write_html(self, fileName):
        with open(fileName, 'w', encoding='utf-8') as fh:
            fh.write(self.make_html())


class LinkItem(AbcItem):

    def __init__(self, caption, url):
        super().__init__(caption)
        self.url = url


class ListItem(AbcItem):

    def __init__(self, caption):
        super().__init__(caption)
        self.items = []

    def add(self, item):
        self.items.append(item)


# abstractFactory
class Factory(ABC):

    @abstractmethod
    def create_page_item(self, title, author):
        pass

    @abstractmethod
    def create_link_item(self, caption, url):
        pass

    @abstractmethod
    def create_list_item(self, caption):
        pass
