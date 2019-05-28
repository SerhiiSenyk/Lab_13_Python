# -*- coding: utf-8 -*- 

# @author Serhii Senyk

from abc import ABC
#from app import db


class OfficeAppliance(ABC):

    #-----------------------------------------------------------------------------------------#
    def __init__(self, price = 0, color = None, weight = 0, producer = None, material = None):
        self.price = price
        self.color = color
        self.weight = weight
        self.producer = producer
        self.material = material

    def __str__(self):
        return "\tPrice :\t" + str(self.price) + "\n" +\
            "\tColor {" + str(self.color) + "\n\t}\n" +\
            "\tWeight :\t" + str(self.weight) + "\n" +\
            "\tProducer :\t" + str(self.producer) + "\n" +\
            "\tMaterial :\t" + str(self.material)






