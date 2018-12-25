# Retail class contains 3 attributes - Item description, units in inventory, and price.

class Retail:
    def __init__(self, unitName, unitDesc, numUnits, unitPrice): # Object initialization
        self.__unitName = unitName; # Unit name
        self.__unitDesc = unitDesc; # Unit description
        self.__numUnits = numUnits; # Unit quantity
        self.__unitPrice = unitPrice; # Unit price

    def setName(self, name): # Set unit name
        self.__unitName = name;

    def setDescription(self, description): # Set unit description
        self.__unitDesc = description;

    def setUnits(self, units): # Set unit quantity
        self.__numUnits = units;

    def setPrice(self, price): # Set unit price
        self.__unitPrice = price;

    def getName(self): # Get unit name
        return self.__unitName;

    def getDescription(self): # Get unit description
        return self.__unitDesc;

    def getUnits(self): # Get quantity of units
        return self.__numUnits;

    def getPrice(self): # Get unit price
        return self.__unitPrice;

