# -*- coding: utf-8 -*-  

# @author Serhii Senyk
from models.OfficeAppliance import OfficeAppliance
from models.Color import Color
from models.Size import Size

class Board(OfficeAppliance):

    def __init__(self, price = 0, color = Color(), weight = 0, producer = None, material = None,
                 surface = None, size_of_surface = Size(), type_of_frame = None):
        super().__init__(price, color, weight, producer, material)
        self.surface = surface
        self.size_of_surface = size_of_surface
        self.type_of_frame = type_of_frame

    def __str__(self):
        return "Board {\n" + super().__str__() +\
            "\n\tSurface :\t" + str(self.surface) +\
            "\n\tSize of surface {" + str(self.size_of_surface) + "\n\t}"+\
            "\n\tType of frame :\t" + str(self.type_of_frame) + "\n}\n"



