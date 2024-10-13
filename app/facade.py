from modules.product import Product
from modules.get_subcategory import get_subcategory
from db.access_reader import AccessReader


def read_db(db_filepath: str) -> list[Product]:
    """
    Считывает данные из БД Access
    :param db_filepath: путь до БД
    :return: список объектов Product (перенос записей таблиц в объекты)
    """
    access_reader = AccessReader()
    db_records = access_reader.read_all(db_filepath)
    products = []
    for record in db_records:
        products.append(Product(record[0], record[1], record[6], record[5], parameters=record[4], gost=record[3],
                                marking=record[2]))
    return products


def get_subcategories(products: list[Product]) -> dict:
    """
    Разделяет товары по подкатегориям ОКПД2
    :param products: список объектов Product
    :return: список подкатегорий с товарами, объединенными по ОКПД2
    """
    subcategory = get_subcategory(products)
    return subcategory


def get_groups(subcategory_products: list[Product]) -> list[str]:
    """
    Выделяет группы для товаров одной подкатегории
    :param subcategory_products: список товаров одной подкатегории
    :return: список групп для данной подкатегории
    """
    return ["группа 1", "группа 2", "группа 3"]


def choose_group(product: Product, groups: list[str]) -> str:
    """
    Для товара выбирает группу, к которой его следует отнести
    :param product: товар
    :param groups: группы для подкатегории, к которой относится товар
    :return: группа, к которой товар должен быть отнесен
    """
    return "группа 1"


def get_group_properties(group_products: list[Product]) -> list[str]:
    """
    Для группы с товарами выделяет свойства группы
    :param group_products: группа с товарами в ней
    :return: свойства для данной группы
    """
    return ["свойство 1", "свойство 2", "свойство 3"]


def get_product_with_properties(product: Product, properties: list[str]) -> Product:
    """
    Заполняет словарь properties у товара в соответствии с переданными свойствами, выделяя свойства товара из строки параметров
    :param product: товар
    :param properties: свойства группы товара, в которые необходимо разложить параметры товара
    :return:
    """
    product.properties["свойство 1"] = "параметр 1"
    product.properties["свойство 2"] = "параметр 2"
    product.properties["свойство 3"] = "параметр 3"
    return product


def save_table(products: list[Product], group_name: str, properties: list[str]):
    """
    Создает таблицу группы в БД, сохраняет товары в ней
    :param products: список товаров
    :param group_name: название группы, к которой относятся товары
    :param properties: список свойств группы
    :return:
    """
    pass
