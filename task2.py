# TODO Найдите количество книг, которое можно разместить на дискете

fdd_capacity_mb = 1.44
total_pages = 100
total_lines = 50
total_symbols = 25
one_symbol_weight_b = 4
ONE_MB = 1024
ONE_KB = 1024

one_page_weight_b = total_lines * total_symbols * one_symbol_weight_b
one_book_weight_b = total_pages * one_page_weight_b
total_amount_of_books = fdd_capacity_mb * ONE_MB * ONE_KB // one_book_weight_b
print("Количество книг, помещающихся на дискету:", round(total_amount_of_books))
