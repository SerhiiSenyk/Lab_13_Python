# -*- coding: utf-8 -*- 

# @author Serhii Senyk
from managers.SortType import SortType
from models.Color import Color

class OfficeAppliancesManager:

    def __init__(self, office_appliances = None):
        self.office_appliances = office_appliances

    def find_by_color(self, color = Color()):
        return list(filter(lambda office_appliance: office_appliance.color == color, self.office_appliances))

    def sort_by_price(self, office_appliances, sort_type = SortType.ASCENDING):
        if sort_type == SortType.ASCENDING:
              office_appliances.sort(key = lambda office_appliance: office_appliance.price, reverse = False)
        else :
              office_appliances.sort(key = lambda office_appliance: office_appliance.price, reverse = True)

    def sort_by_weight(self, office_appliances, sort_type = SortType.ASCENDING):
        if sort_type == SortType.ASCENDING:
              office_appliances.sort(key = lambda office_appliance: office_appliance.weight, reverse = False)
        else :
              office_appliances.sort(key = lambda office_appliance: office_appliance.weight, reverse = True)
    

