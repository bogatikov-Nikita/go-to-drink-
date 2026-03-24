def find_first_index(products, product_name):
    """
    Возвращает индекс первого вхождения товара
    Если товар не найден - возвращает None
    """
    for position, item in enumerate(products):
        if item == product_name:
            return position
    return None

products_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

search_items = ['банан', 'груша', 'персик']

for product in search_items:
    product_index = find_first_index(products_list, product)
    if product_index is not None:
        print(f"Первое вхождение товара '{product}' имеет индекс {product_index}.")
    else:
        print(f"Товар '{product}' не найден в списке.")