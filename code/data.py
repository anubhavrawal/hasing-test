#Class for represnting the weapon extrated from the bag. And all the feature of the weapon
class Data:
    def __init__(self, itemName, minStrength, maxStrength, rarity):
        self.itemName = itemName
        self.minStrength = minStrength
        self.maxStrength = maxStrength
        self.rarity = rarity
    
    def print_cont(self):
        print("%s %s, %s %s"%(self.rarity, self.itemName,self.minStrength,self.maxStrength))\


