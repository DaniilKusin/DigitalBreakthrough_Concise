def print_products(subcategory_products: dict):
    i = 0
    for key, values in subcategory_products.items():
        if i == 3:
            for i in range(len(values)):
                p = values[i]
                print(p.okpd2, p.name)
            print(len(values))
            break
        i += 1
