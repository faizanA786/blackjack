import random

class newTrumpCard:
    def __init__(self):
        self.trumpVal = self.randTrump()
        self.name = self.getName(self.trumpVal)
        self.desc = self.getDesc(self.trumpVal)

    def randTrump(self):
        random.seed()
        trumpVal = 0
        match trumpVal:
            case 0:
                trumpVal = 0
            case 2:
                trumpVal = "Ace"
            case 3:
                trumpVal = "Hearts"
            case 4:
                trumpVal = "Clubs"
        return trumpVal
    
    def getName(self, trumpVal):
        match trumpVal:
            case 0:
                return "27"
            
    def getDesc(self, trumpVal):
        match trumpVal:
            case 0:
                return "Increases the cap to from 21 to 27"
