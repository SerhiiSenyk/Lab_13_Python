# @author Serhii Senyk

from enum import Enum, unique

@unique
class Material(Enum):

    METAL = 1
    PLASTIC = 2
    METAL_PLUS_PLASTIC = 3
