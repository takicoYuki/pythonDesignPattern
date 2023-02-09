from collections.abc import Iterator, Iterable

class Book:

  def __init__(self, name):
    self.__name = name

  def get_name(self):
    return self.__name

class BookShelf(Iterable):

  def __init__(self):
    self.__books = []

  def append_book(self, book: Book):
    self.__books.append(book)

  def get_book_at(self, index):
    return self.__books[index]

  # ループ文の際にIteratorとしてまわしてくれる
  def __iter__(self):
    return BookShelfIterator(self)

class BookShelfIterator(Iterator):

  def __init__(self, book_shelf: BookShelf):
    self.__book_shelf = book_shelf
    self.__index = 0

  def __next__(self):
    try:
      book = self.__book_shelf.get_book_at(self.__index)
      self.__index += 1
    except IndexError:
      # Iterator処理が修了する
      raise StopIteration()
    return book

book_shelf = BookShelf()
book_shelf.append_book(Book('Dragon Ball 1'))
book_shelf.append_book(Book('Dragon Ball 2'))
book_shelf.append_book(Book('Dragon Ball 3'))
book_shelf.append_book(Book('Dragon Ball 4'))
book_shelf.append_book(Book('Dragon Ball 5'))

for book in book_shelf:
  # __iter__ -> __next__が自動で呼び出される
  print(book.get_name())
