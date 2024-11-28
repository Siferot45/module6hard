from Figure import Figure

class Cube(Figure):
    sides_count = 12
    
    def __init__(self, color, *sides):
        super().__init__(color, sides)
    