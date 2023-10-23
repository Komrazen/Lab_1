# TODO Найдите количество книг, которое можно разместить на дискете
bt = 1 # Это байт, а не бит!
kbt = 1024
mbt = 1024 * kbt
vol_pages = 100
vol_str = 50
vol_symb = 25
symb = 4 * bt
vol_disk = 1.44 * mbt
all_symb = symb * vol_symb * vol_str * vol_pages
books = vol_disk // all_symb
print("Количество книг, помещающихся на дискету:", int(books))
