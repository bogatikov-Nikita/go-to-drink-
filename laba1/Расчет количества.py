# Объем дискеты в Мб
disk_size_mb = 1.44

# Параметры книги
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Перевод объема дискеты в байты
disk_size_bytes = disk_size_mb * 1024 * 1024

# Расчет количества символов в книге
total_chars = pages * lines_per_page * chars_per_line

# Расчет объема одной книги в байтах
book_size_bytes = total_chars * bytes_per_char

# Расчет количества книг (целое число)
num_books = int(disk_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", num_books)

