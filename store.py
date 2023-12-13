import doctest

import doctest


class Car:
    def __init__(self, brand: str, model: str, fuel_tank_capacity: float, current_fuel_level: float):
        """
        Создание и подготовка к работе объекта "Машина"

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param fuel_tank_capacity: Объем топливного бака
        :param current_fuel_level: Текущий уровень топлива

        Примеры:
        >>> car = Car("Toyota", "Camry", 60, 30)  # инициализация экземпляра класса
        """
        if not isinstance(fuel_tank_capacity, (int, float)):
            raise TypeError("Объем топливного бака должен быть типа int или float")
        if fuel_tank_capacity <= 0:
            raise ValueError("Объем топливного бака должен быть положительным числом")
        self.fuel_tank_capacity = fuel_tank_capacity

        if not isinstance(current_fuel_level, (int, float)):
            raise TypeError("Текущий уровень топлива должен быть int или float")
        if not (0 <= current_fuel_level <= fuel_tank_capacity):
            raise ValueError("Текущий уровень топлива должен быть в пределах от 0 до объема топливного бака")
        self.current_fuel_level = current_fuel_level

        self.brand = brand
        self.model = model

    def drive(self, distance: float) -> None:
        """
        Проехать определенное расстояние на машине.

        :param distance: Расстояние для преодоления

        :raise ValueError: Если расстояние превышает текущий уровень топлива, вызываем ошибку

        Примеры: Условием конкретной задачи необходимо определить расход топлива
        """
        car = Car("Toyota", "Camry", 60, 40)
        car.drive(200)

        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние в км должно быть int или float")
        if car.current_fuel_level * 6 < distance:  # Пуcть 6 = const = расход топлива (можно сделать полем)
            raise ValueError("Текущуго количества топлива не хватит на дистанцию")
        ...

    def refuel(self, fuel_amount: float) -> None:
        """
        Пополнить топливо в баке.

        :param fuel_amount: Количество добавляемого топлива

        :raise ValueError: Если количество добавляемого топлива превышает свободное место в баке, вызываем ошибку

        Примеры:
        """
        car = Car("Toyota", "Camry", 60, 40)
        car.refuel(20)

        if not isinstance(fuel_amount, (int, float)):
            raise TypeError("Количество литров топлива должно быть int или float")
        if car.fuel_tank_capacity - car.current_fuel_level < fuel_amount:
            raise ValueError("Заливааемое топливо превышает объём бака")
        ...

    def get_mileage(self) -> float:
        """
        Получить пробег машины.

        :return: Пробег машины

        Примеры:
        >>> car = Car("Toyota", "Camry", 60, 40)
        >>> car.get_mileage()
        """
        ...

    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации
