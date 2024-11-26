class Figure:
    sides_count = 0
    
    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = list(sides)
        self. filled = False
        
    def get_color(self):
        return self.__color
        
    def __is_valid_color(self, r, g, b):
        new_rgb = []
        for element_rgb in [r, g, b]:
            if isinstance(element_rgb, int) and 0 <= element_rgb <= 255 :
                    new_rgb.append(element_rgb)
        if len(new_rgb) == 3:
            return new_rgb
        
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print(f"Invalid color values: ({r}, {g}, {b})")
            

    def __is_valid_sides(self, *new_sides):
        
        is_valid = True

        for side in new_sides:
            if isinstance(side, int) and 0 < side:
                pass
            
        return is_valid
                
    def get_sides(self):
        return self.__sides
    
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides == new_sides
        else:
            print("Invalid sides or incorrect number of sides")
        


