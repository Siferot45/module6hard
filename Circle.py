from Figure import Figure

class Circle(Figure):
    sides_count = 1
    
    def __init__(self, color, *sides):
        super().__init__(color, sides)
