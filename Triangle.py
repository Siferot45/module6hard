from Figure import Figure

class Triangle(Figure):
    
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, sides)