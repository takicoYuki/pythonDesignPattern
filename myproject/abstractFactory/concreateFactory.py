# concreteFactory

from abstractFactory import (
  LinkItem, ListItem, PageItem, Factory
)


class HtmlPageItem(PageItem):

    def __init__(self, title, author):
        super().__init__(title, author)

    def make_html(self):
        output = '<html>\n<head>\n<title>{}</title>\n</head>\n'.format(self.title)
        output += '<body>\n'
        output += '<h1>{}</h1>\n'.format(self.title)
        output += '<ul>'
        for list_item in self.content:
            output += list_item.make_html()
        output += '</ul>\n'
        output += '<hr>\n<address>{}</address>\n'.format(self.author)
        output += '</body>/n</html>\n'
        return output


class HtmlLinkItem(LinkItem):

    def __init__(self, caption, url):
        super().__init__(caption, url)

    def make_html(self):
        return '<li><a href= "{}">{}</a></li>'.format(self.url, self.caption)


class HtmlListItem(ListItem):

    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        output = '<li>\n'
        output += self.caption + '\n'
        output += '<ul>\n'
        for link_item in self.items:
            output += link_item.make_html()
        output += '</ul>\n'
        output += '</li>\n'
        return output


class HtmlFactory(Factory):

    def create_page_item(self, title, author):
        return HtmlPageItem(title, author)

    def create_link_item(self, caption, url):
        return HtmlLinkItem(caption, url)

    def create_list_item(self, caption):
        return HtmlListItem(caption)


html_factory = HtmlFactory()

asahi = html_factory.create_link_item('朝日新聞', 'http://asahi')
yomiuri = html_factory.create_link_item('読売新聞', 'http://yomiuri')
yahoo = html_factory.create_link_item('yahoo', 'http://yahoo')

news_page = html_factory.create_list_item('新聞')
news_page.add(asahi)
news_page.add(yomiuri)

other_pages = html_factory.create_list_item('その他ページ')
other_pages.add(yahoo)

all_page = html_factory.create_page_item('My Page', 'taro')
all_page.add(news_page)
all_page.add(other_pages)

all_page.write_html('tmp.html')
