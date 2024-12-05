from Circle import Circle
from Cube import Cube
from Triangle import Triangle

# Проверка работы

triangle = Triangle((500, 220, 190), 12)
circle = Circle((200, 200, 100), 10)
cube = Cube((123, 220, 250), 12)
print(cube.get_sides())

# Проверка на изменение цветов:
circle.set_color(55, 66, 707) 
print(circle.get_color())

triangle.set_color(88, 66, 90) 
print(triangle.get_color())

# Проверка на изменение сторон:
circle.set_sides(3) 
print(circle.get_sides())

triangle.set_sides(3,4,5) 
print(triangle.get_sides())

# Проверка периметра (круга), это и есть длина:
#e = len(triangle)
#print(len(circle))
            #return "Сумма сторон фигуры:", sum_figure
print(len(triangle))
print(cube.get_volume())
print(triangle.get_square())
