# -*- coding: utf-8 -*- 

# @author Serhii Senyk

class Color:

    def __init__(self, red = 0, green = 0, blue = 0):
        self.red = red
        self.green = green
        self.blue = blue

    def __eq__(self, other):
        if isinstance(other, Color):
            return(self.red == other.red and
                   self.green == other.green and
                   self.blue == other.blue)
        return NotImplemented

    def __str__(self):
        return "\n\t\tred :\t" + str(self.red) +\
            "\n\t\tgreen :\t" + str(self.green) +\
            "\n\t\tblue :\t" + str(self.blue)

