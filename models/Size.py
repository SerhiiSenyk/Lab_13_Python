# -*- coding: utf-8 -*- 

# @author Serhii Senyk

class Size:

    def __init__(self, lenght = 0, width = 0, height = 0):
         self.lenght = lenght;
         self.width = width;
         self.height = height;

    def __eq__(self, other):
        if isinstance(other, Size):
            return (self.lenght == other.lenght and
                        self.width == other.width and
                        self.height == other.height)
        return NotImplemented

    def __str__(self):
        return "\n\t\tlenght :\t" + str(self.lenght) +\
            "\n\t\twidth :\t\t" + str(self.width) +\
            "\n\t\theight :\t" + str(self.height)
