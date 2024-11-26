from Circle import Circle

# Проверка работы
circle1 = Circle((200, 200, 100), 10)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 707) 
print(circle1.get_color())

# Проверка на изменение сторон:
circle1.set_sides(15) # Изменится
print(circle1.get_sides())