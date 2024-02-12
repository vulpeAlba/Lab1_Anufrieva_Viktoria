class Appliances:
    """
    Базовый класс для бытовой техники.
    """

    def __init__(self, brand: str, model: str, price: float):
        """
        Инициализация объекта Appliances

        :param brand: Бренд техники
        :param model: Модель техники
        :param price: Цена техники (P)
        """
        self.brand = brand
        self.model = model
        self.price = price

    def run(self) -> None:
        """
        Выполняется запуск устройства
        """
        pass

    def mod(self) -> None:
        """
        Изменяется режим работы устройства
        """
        pass

    def __str__(self) -> str:
        """
        Возвращается строковое представление объекта класса
        """
        return f"{self.brand!r} {self.model!r} - P{self.price!r}"

    def __repr__(self) -> str:
        """
        Возвращается формальное строковое представление объекта класса
        """
        return f"{self.__class__.__name__!r}(brand={self.brand!r}, model={self.model!r}, price={self.price!r})"


class Refrigerator(Appliances):
    """
    Дочерний класс для холодильников
    """

    def __init__(self, brand: str, model: str, price: float, height: int, capacity: int):
        """
        Инициализация объекта Refrigerator

        :param brand: Бренд холодильника
        :param model: Модель холодильника
        :param price: Цена холодильника (Р)
        :param height: Высота холодильника
        :param capacity: Вместительность холодильника
        """
        super().__init__(brand, model, price)
        self.height = height
        self.capacity = capacity

    def run(self) -> None:
        """
        Выполняет запуск холодильника

        Метод необходимо перегрузить, т.к. запуск всех устройств происходит по-разному
        """
        pass

    def mod(self) -> None:
        """
        Изменяется режим работы устройства

        Метод необходимо перегрузить, т.к. настройка всех устройств происходит по-разному
        """
        pass

    def open_time_check(self, time: int, opened_flag: bool) -> None:
        """
        Издаётся сигнал, если холодильник открыт слишком долго

        :param time: Разрешенное время удержания холодильника открытым
        :param opened_flag: Флаг - показания датчика, открыт ли холодильник
        """
        # Реализация вызова
        pass

    def __repr__(self) -> str:
        """
        Перегруженный метод

        :return: Формальное строковое представление объекта Холодильник
        """
        return f"{self.__class__.__name__}(brand={self.brand}, model={self.model}, price={self.price}, " \
               f"height={self.height}, capacity={self.capacity})"


class RobotVacuumCleaner(Appliances):
    """
    Дочерний класс для пылесосов
    """

    def __init__(self, brand: str, model: str, price: float, battery_capacity: int, app_for_connection: str):
        """
        Инициализация объекта RobotVacuumCleaner

        :param brand: Бренд пылесоса
        :param model: Модель пылесоса
        :param price: Цена пылесоса (Р)
        :param battery_capacity: Ёмкость аккумулятора в пылесосе
        :param app_for_connection: Название приложения для подключения пылесоса к смартфону
        """
        super().__init__(brand, model, price)
        self.battery_capacity = battery_capacity
        self.app_for_connection = app_for_connection

    def run(self) -> None:
        """
        Выполняет запуск пылесоса

        Метод необходимо перегрузить, т.к. запуск всех устройств происходит по-разному
        """
        pass

    def mod(self) -> None:
        """
        Изменяется режим работы устройства

        Метод необходимо перегрузить, т.к. настройка всех устройств происходит по-разному
        """
        pass

    def signal(self, action_name: str) -> None:
        """
        Запускается голосовой сигнал (фраза) в соответствии с выполняемым действием

        :param action_name: Название программы.
        """
        pass

    def __repr__(self) -> str:
        """
        Перегруженный метод

        :return: Формальное строковое представление пылесоса
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, price={self.price!r}, " \
               f"battery_capacity={self.battery_capacity!r}, app_for_connection={self.app_for_connection!r})"



