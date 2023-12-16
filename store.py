import doctest


class Store:
    def __init__(self, name: str, floor_area: float, products: dict, product_capacity: int):
        """
        Создание и подготовка к работе объекта "Магазин"

        :param name: Название магазина
        :param floor_area: Общая площадь магазина
        :param products: Словарь с продуктами и их количеством в магазине

        Примеры:
        >>> store = Store("Grocery Store", 1000, {"Apples": 50, "Bread": 100}, 300)  # инициализация экземпляра класса
        """
        if not isinstance(floor_area, (int, float)):
            raise TypeError("Площадь магазина должна быть типа int или float")
        if floor_area <= 0:
            raise ValueError("Площадь магазина должна быть положительным числом")
        self.floor_area = floor_area

        if not isinstance(products, dict):
            raise TypeError("Продукты должны быть представлены в виде словаря")
        self.products = products

        if not isinstance(product_capacity, int):
            raise TypeError("Вместимость магазина должна быть типа int")
        if floor_area <= 0:
            raise ValueError("Вместимость магазина должна быть положительным числом")
        self.product_capacity = product_capacity

        self.name = name

    def add_product(self, product_name: str, quantity: int) -> None:
        """
        Добавление продукта в магазин.

        :param product_name: Название продукта
        :param quantity: Количество добавляемого продукта

        :raise ValueError: Если количество добавляемого продукта превышает свободное место в магазине, вызываем ошибку

        Примеры:
        """
        store = Store("Grocery Store", 1000, {"Apples": 50, "Bread": 100}, 300)
        store.add_product("Milk", 20)

        if not isinstance(quantity, int):
            raise TypeError("Количество добавляемого товара должно быть int")
        if store.product_capacity < sum(store.products.values()) + quantity:
            raise ValueError("Добавляемому товару не хватит места в магазине")
        ...

    def sell_product(self, product_name: str, quantity: int) -> None:
        """
        Продажа продукта из магазина.

        :param product_name: Название продукта
        :param quantity: Количество продукта для продажи

        *Можно подсчитывать количество товаров и добавить проверку на лимит продуктов в магазине
        :raise ValueError: Если количество продукта для продажи превышает количество доступного продукта, вызываем ошибку

        Примеры:
        """
        store = Store("Grocery Store", 1000, {"Apples": 50, "Bread": 100}, 300)
        store.sell_product("Apples", 10)

        if not isinstance(quantity, int):
            raise TypeError("Количество добавляемого товара должно быть int")
        if store.products[product_name] < quantity:
            raise ValueError("Запрашиваемого товара не хватает в магазине")
        ...

    def calculate_revenue(self) -> float:
        """
        Рассчитать выручку магазина.

        :return: Выручка магазина

        Примеры:
        >>> store = Store("Grocery Store", 1000, {"Apples": 50, "Bread": 100}, 300)
        >>> store.calculate_revenue()
        """
        ...

    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации
