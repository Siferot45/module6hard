from Circle import Circle
from Triangle import Triangle

# Проверка работы
circle = Circle((200, 200, 100), 10)
triangle = Triangle((500, 220, 190), 10)

# Проверка на изменение цветов:
circle.set_color(55, 66, 707) 
print(circle.get_color())

triangle.set_color(88, 66, 90) 
print(triangle.get_color())

# Проверка на изменение сторон:
circle.set_sides(3) 
print(circle.get_sides())

triangle.set_sides(3, 'd', 3) 
print(triangle.get_sides())

# Проверка периметра (круга), это и есть длина:

print(len(circle))
print(len(triangle))