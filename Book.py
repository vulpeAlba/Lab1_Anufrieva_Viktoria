class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_  # Идентификатор книги
        self.name = name  # Название книги
        self.pages = pages  # Количество страниц в книге

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id_}, name="{self.name}f", pages={self.pages})'

