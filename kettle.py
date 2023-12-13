import doctest


class Kettle:
    def __init__(self, capacity: float, water_level: float, temperature: float):
        """
        Создание и подготовка к работе объекта "Чайник"
        :param capacity: Объем чайника
        :param water_level: Уровень воды в чайнике
        :param temperature: температура воды в чайнике

        Примеры:
        >>> kettle = Kettle(1000, 0, 10.5)  # инициализация экземпляра класса
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Объем чайника должен быть типа int или float")
        if capacity <= 0:
            raise ValueError("Объем чайника должен быть положительным числом")
        self.capacity = capacity

        if not isinstance(water_level, (int, float)):
            raise TypeError("Уровень воды должен быть int или float")
        if not (0 <= water_level <= capacity):
            raise ValueError("Уровень воды должен быть в пределах от 0 до объема чайника")
        self.water_level = water_level

        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура воды должна быть int или float")
        if not (0 <= temperature <= 100):
            raise ValueError("Температура воды олжна быть в пределах от 0 до макс.температуры в чайнике")
        self.temperature = temperature

    def is_empty_kettle(self) -> bool:
        """
        Функция которая проверяет, является ли чайник пустым

        :return: Является ли чайник пустым

        Примеры:
        >>> kettle = Kettle(1000, 0, 10.5)
        >>> kettle.is_empty_kettle()
        """
        ...

    def boil_water(self, high_temp: float) -> None:
        """
        Закипятить воду в чайнике.

        :param high_temp: желаемая температура после кипячения

        Примеры:
        """
        kettle = Kettle(1000, 500, 10.5)
        kettle.boil_water(100)

        if not isinstance(high_temp, (int, float)):
            raise TypeError("Температура воды должна быть типа int или float")
        if high_temp > 100 or high_temp < kettle.temperature:
            raise ValueError("Температура воды должна быть в пределах возможностей чайника")
        ...

    def pour_tea(self, cups: int) -> None:
        """
        Налить чай в чашки.

        :param cups: Количество чашек (можно реализовать отдельным классом с полем volume)

        :raise ValueError: Если количество чашек больше доступного объема чайника, вызываем ошибку

        Примеры:
        >>> kettle = Kettle(1000, 1000, 10.5)
        >>> kettle.pour_tea(4)
        """
        # Нужна проверка на суммарный объём чашек, чтобы он не превышал объём воды в чайнике
        # То, как она будет описана, зависит от полей класса чашки
        ...

    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации
