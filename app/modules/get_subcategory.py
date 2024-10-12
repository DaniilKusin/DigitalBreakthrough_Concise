from .product import Product


def get_subcategory(products: list[Product]) -> dict[str, list[Product]]:

    groups = {}

    for product in products:
        okpd2_code = product.okpd2

        if okpd2_code not in groups:
            groups[okpd2_code] = []

        groups[okpd2_code].append(product)

    return groups
