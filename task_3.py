# TODO Найдите количество книг, которое можно разместить на дискете

fdd_capacity_MB = 1.44
total_pages_ = 100
total_lines_ = 50
total_symbols_ = 25
one_symbol_weight_B = 4
one_MB = 1024
one_KB = 1024

one_page_weight_B = total_lines_ * total_symbols_ * one_symbol_weight_B
one_book_weight_B = total_pages_ * one_page_weight_B
total_amount_of_books = fdd_capacity_MB * one_MB * one_KB // one_book_weight_B
print("Количество книг, помещающихся на дискету:", round(total_amount_of_books))
