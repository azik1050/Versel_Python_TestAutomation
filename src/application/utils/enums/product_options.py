from enum import Enum


class ProductColor(str, Enum):
    BLACK = "Black"
    WHITE = "White"
    BLUE = "Blue"


class ProductSize(str, Enum):
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"
    XXXL = "XXXL"
