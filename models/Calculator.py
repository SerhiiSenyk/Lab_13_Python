# -*- coding: utf-8 -*- 

# @author Serhii Senyk

from models.OfficeAppliance import OfficeAppliance
from models.Color import Color
from models.Size import Size

class Calculator(OfficeAppliance):

    def __init__(self, price = 0, color = Color(), weight = 0, producer = None, material = None,
                 type = None, bit_size = 0, corpus_size = Size()):
        super().__init__(price, color, weight, producer, material)
        self.type = type
        self.bit_size = bit_size
        self.corpus_size = corpus_size

    def __str__(self):
        return "Calculator {\n" + super().__str__() +\
            "\n\tType :\t" + str(self.type) +\
            "\n\tBit size :\t" + str(self.bit_size) +\
            "\n\tCorpus size {" + str(self.corpus_size) + "\n\t}\n}\n"


