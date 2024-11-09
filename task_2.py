amount_pages = 100 # Кол-во страниц в 1 книге
amount_strings = 50 # Число строк на странице
amount_symb = 25 # Кол-во символов в строке
size_one_symbol = 4 # Вес одного символа
size_all_symbol = amount_pages * amount_strings * amount_symb * size_one_symbol
size_all_symbol_in_mb = size_all_symbol/( 1024 * 1024) # Итого вес символов в мегабайтах
size_dick = 1.44 # Объем диска в мегабайтах
number_books = size_dick // size_all_symbol_in_mb
print("Количество книг, помещающихся на дискету:", round(number_books))
