# -*- coding: utf-8 -*- 

# @author Serhii Senyk

from models.OfficeAppliance import OfficeAppliance
from models.Color import Color

class StationeryKnife(OfficeAppliance):

    #width_of_blade =  db.Column(db.Integer)
    #------------------------------------------------------------------------------------------#
    def __init__(self, price = 0, color = Color(), weight = 0, producer = None, material = None,
                 width_of_blade = 0.0):
        super().__init__(price, color, weight, producer, material)
        self.width_of_blade = width_of_blade

    def __str__(self):
        return "Stationery knife {\n" + super().__str__() +\
            "\n\tWidth of blade :\t" + str(self.width_of_blade) + "\n}\n"


