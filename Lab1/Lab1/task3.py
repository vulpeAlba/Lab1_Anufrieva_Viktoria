# TODO Найдите количество книг, которое можно разместить на дискете
INF_AMOUNT = 1.44 * 1024 * 1024
SHEETS_NUM = 100
LINES_NUM = 50
SYMBOLS_NUM = 25
SYMB_IN_BYTES = 4

amount = SYMBOLS_NUM * SYMB_IN_BYTES * LINES_NUM * SHEETS_NUM
count_books = INF_AMOUNT // amount
print("Количество книг, помещающихся на дискету:", count_books)
