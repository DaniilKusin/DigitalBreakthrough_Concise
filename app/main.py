from facade import *
from app.test.print_products import print_products


def main():
    products = read_db('./data/accdb/spravochnik_tovarov.accdb')
    subcategory_products = get_subcategories(products)

    print_products(subcategory_products)

    subcategory_groups = {}
    for subcategory_name, prods in subcategory_products.items():
        subcategory_groups[subcategory_name] = get_groups(prods)

    subcategory_groups_products = {}
    for subcategory_name, prods in subcategory_products.items():
        subcategory_groups_products[subcategory_name] = {}
        for g in subcategory_groups[subcategory_name]:
            if g not in subcategory_groups_products[subcategory_name]:
                subcategory_groups_products[subcategory_name][g] = []
        for p in prods:
            prod_group = choose_group(p, subcategory_groups[subcategory_name])
            subcategory_groups_products[subcategory_name][prod_group].append(p)

    subcategory_group_properties = {}
    for subcategory_name, groups in subcategory_groups_products.items():
        for group_name, group_products in groups.items():
            subcategory_group_properties[subcategory_name] = {}
            subcategory_group_properties[subcategory_name][group_name] = get_group_properties(group_products)

    for subcategory_name, subc_groups in subcategory_groups_products.items():
        for group_name, products in subc_groups.items():
            for prod in products:
                subc_groups[prod] = get_product_with_properties(prod, subcategory_group_properties[subcategory_name][
                    group_name])

    for subcategory_name, subc_groups in subcategory_groups_products.items():
        for group_name, products in subc_groups.items():
            save_table(products, group_name, subcategory_group_properties[subcategory_name][group_name])


if __name__ == '__main__':
    main()
