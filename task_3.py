# TODO Найдите количество книг, которое можно разместить на дискете

FDD_weight_MD = 1.44
pages_ = 100
lines_ = 50
symbols_ = 25
one_symbol_weight_B = 4
one_MB = 1024
one_KB = 1024

one_page_weight_B = lines_ * symbols_ * one_symbol_weight_B
one_book_weight_B = pages_ * one_page_weight_B
FDD_weight_B = FDD_weight_MD * one_MB * one_KB
total_amount_of_books = FDD_weight_B // one_book_weight_B
print("Количество книг, помещающихся на дискету:", round(total_amount_of_books))
