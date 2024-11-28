
class Figure:
    sides_count = 0
    
    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = self.init_sides(*sides)
        self. filled = False
        
    def init_sides(self, *sides):
        
        list_sides = [*sides[0]]

        if len(list_sides) == self.sides_count:
            self.__sides = list(sides)
        elif len(list_sides) == 1:
            self.__sides = list(sides[0]) * self.sides_count
        else:
            self.__sides = list(1) * self.sides_count
    # else:
    #     print("Unacceptable sides")

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
                        
    def get_sides(self):
        return self.__sides
    
    def __is_valid_sides(self, *new_sides):
        is_valid = False
        
        if len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides):
             is_valid = True

        return is_valid
    
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
            
        else:
            print("Invalid sides or incorrect number of sides")
            
    def __len__(self):
        
        if (isinstance(x, int)  for x in self.__sides):
            return sum(self.__sides)
        else:
            print(self.__sides)
            print(type(self.__sides))
       
        


