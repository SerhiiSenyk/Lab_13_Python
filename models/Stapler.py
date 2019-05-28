# -*- coding: utf-8 -*- 

# @author Serhii Senyk

from models.OfficeAppliance import OfficeAppliance
from models.Color import Color

class Stapler(OfficeAppliance):

    def __init__(self, price = 0, color = Color(), weight = 0, producer = None, material = None,
                 staples_size = 0, power = 0):
        super().__init__(price, color, weight, producer, material)
        self.staples_size = staples_size
        self.power = power

    def __str__(self):
        return "Stapler {\n" + super().__str__() +\
            "\n\tStaples size :\t" + str(self.staples_size ) +\
            "\n\tPower :\t" + str(self.power) + "\n}\n"
        
