from facade import *
from test.print_products import print_products


def main():
    # Чтение данных из БД и формирование списка товаров из объектов Product
    products = read_db('./data/accdb/spravochnik_tovarov.accdb')

    # Разделение товаров на подкатегории согласно ОКПД2
    subcategory_products = get_subcategories(products)

    # Получение групп для каждой подкатегории в виде {"ОКПД2": ["группа 1", "группа 2", ]}
    subcategory_groups = {}
    for subcategory_name, prods in subcategory_products.items():
        subcategory_groups[subcategory_name] = get_groups(prods)

    # Получение товаров для каждой группы в подкатегории
    # в виде {"ОКПД2": {"группа 1": [Product 1, Product 2, ], }}
    subcategory_groups_products = {}
    for subcategory_name, prods in subcategory_products.items():
        subcategory_groups_products[subcategory_name] = {}
        for g in subcategory_groups[subcategory_name]:
            if g not in subcategory_groups_products[subcategory_name]:
                subcategory_groups_products[subcategory_name][g] = []
        for p in prods:
            prod_group = choose_group(p, subcategory_groups[subcategory_name])
            subcategory_groups_products[subcategory_name][prod_group].append(p)

    # Получение свойств для каждой группы в подкатегории
    # в виде {"ОКПД2": {"группа 1": ["свойство 1", "свойство 2", ], }}
    subcategory_group_properties = {}
    for subcategory_name, groups in subcategory_groups_products.items():
        subcategory_group_properties[subcategory_name] = {}
        for group_name, group_products in groups.items():
            subcategory_group_properties[subcategory_name][group_name] = get_group_properties(group_products)

    # Перераспределение свойств товара в соответствии со свойствами его группы
    for subcategory_name, subc_groups in subcategory_groups_products.items():
        for group_name, products in subc_groups.items():
            for i in range(len(products)):
                subcategory_groups_products[subcategory_name][group_name][i] = \
                    get_product_with_properties(subcategory_groups_products[subcategory_name][group_name][i],
                                                subcategory_group_properties[subcategory_name][group_name])

    # Сохранение полученных групп с товарами в БД
    for subcategory_name, subc_groups in subcategory_groups_products.items():
        for group_name, products in subc_groups.items():
            save_table(products, group_name, subcategory_group_properties[subcategory_name][group_name])


if __name__ == '__main__':
    main()
