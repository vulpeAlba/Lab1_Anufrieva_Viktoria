class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books  # Список книг

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            last_book = self.books[-1]
            return last_book.id_ + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise "Книги с запрашиваемым id не существует"


# if __name__ == "__main__":
#    library = Library([Book(1, "hh", 9), Book(2, "ii", 9), Book(3, "pp", 9)])
#    print(library.get_next_book_id())  # 4
#    print(library.get_index_by_book_id(3))  # 2
#    print(library.get_index_by_book_id(9))  # Error
