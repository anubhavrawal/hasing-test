#New Class for represnting the items current randomly selected strength of weapon card and other feature of weapon
class newCards:
    def __init__(self, itemName, Strength, rarity):
        self.itemName = itemName
        self.Strength = Strength
        self.rarity = rarity
    
    def print_cont(self):
        print("%s %s, %d"%(self.rarity, self.itemName,self.Strength))