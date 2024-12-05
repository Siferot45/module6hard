class Figure:
    """
    Класс для представления геометрической фигуры с заданным цветом и сторонами.

    Этот класс включает методы для работы с цветом фигуры, сторонами, а также их валидацией.
    Методы позволяют устанавливать и получать атрибуты фигуры, а также проверять корректность данных.

    Атрибуты класса:
        sides_count (int): Количество сторон фигуры. По умолчанию 0.
    
    Атрибуты экземпляра:
        __color (list): Цвет фигуры в формате [r, g, b], где r, g, b - целые числа от 0 до 255.
        __sides (list): Стороны фигуры, представленные как список положительных целых чисел.
        filled (bool): Флаг, указывающий, заполнена ли фигура (по умолчанию False).
    """

    sides_count = 0

    def __init__(self, color, *sides):
        """
        Инициализация фигуры с указанным цветом и сторонами.

        Аргументы:
            color (str): Цвет фигуры, представленный строкой.
            *sides (int): Стороны фигуры. Может быть как один список, так и несколько числовых значений.
        """
        self.__color = list(color)
        self.__sides = self.init_sides(*sides)
        self.filled = False

    def init_sides(self, *sides):
        """
        Инициализация сторон фигуры. Проверяет корректность сторон и их количество.

        Аргументы:
            *sides (int): Стороны фигуры, которые могут быть представлены как одно значение или список.

        Возвращает:
            list: Список сторон фигуры.

        Выводит:
            str: Сообщение об ошибке, если стороны некорректны.
        """
        list_sides = [*sides[0]]
        new_sides = []

        if all(isinstance(side, int) and side > 0 for side in list_sides):
            if len(list_sides) == self.sides_count:
                new_sides = list_sides
            elif len(list_sides) == 1:
                new_sides = [list_sides[0]] * self.sides_count
            else:
                new_sides = [1] * self.sides_count
            return new_sides
        else:
            print("Unacceptable sides")

    def get_color(self):
        """
        Возвращает текущий цвет фигуры.

        Возвращает:
            list: Цвет фигуры в формате [r, g, b].
        """
        return self.__color

    def __is_valid_color(self, r, g, b):
        """
        Проверяет, является ли переданное значение цвета допустимым.

        Аргументы:
            r (int): Значение красного компонента цвета.
            g (int): Значение зеленого компонента цвета.
            b (int): Значение синего компонента цвета.

        Возвращает:
            list: Список с допустимыми значениями цвета [r, g, b], если они корректны.
            None: Если хотя бы одно значение не корректно.
        """
        new_rgb = []
        for element_rgb in [r, g, b]:
            if isinstance(element_rgb, int) and 0 <= element_rgb <= 255:
                new_rgb.append(element_rgb)
        if len(new_rgb) == 3:
            return new_rgb

    def set_color(self, r, g, b):
        """
        Устанавливает цвет фигуры, если значения корректны.

        Аргументы:
            r (int): Значение красного компонента цвета.
            g (int): Значение зеленого компонента цвета.
            b (int): Значение синего компонента цвета.

        Выводит:
            str: Сообщение об ошибке, если значения цвета некорректны.
        """
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print(f"Invalid color values: ({r}, {g}, {b})")

    def get_sides(self):
        """
        Возвращает текущие стороны фигуры.

        Возвращает:
            list: Список сторон фигуры.
        """
        return self.__sides

    def __is_valid_sides(self, *new_sides):
        """
        Проверяет, являются ли переданные стороны допустимыми.

        Аргументы:
            *new_sides (int): Стороны фигуры, представленные целыми положительными числами.

        Возвращает:
            bool: True, если стороны корректны, иначе False.
        """
        is_valid = False
        if len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides):
            is_valid = True
        return is_valid

    def set_sides(self, *new_sides):
        """
        Устанавливает новые стороны фигуры, если они корректны.

        Аргументы:
            *new_sides (int): Стороны фигуры.

        Выводит:
            str: Сообщение об ошибке, если стороны некорректны.
        """
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print(f"Invalid sides or incorrect number of sides: {new_sides}")

    def __len__(self):
        """
        Возвращает периметр фигуры, который равен сумме всех её сторон.

        Возвращает:
            int: Сумма сторон фигуры (периметр).

        Выводит:
            str: Сообщение об ошибке, если стороны некорректны.
        """
        if all(isinstance(x, int) for x in self.__sides):
            sum_figure = sum(self.__sides)
            return sum_figure
        
        else:
            print(self.__sides)
