import random

class newTrumpCard:
    def __init__(self):
        self.trumpVal = self.randTrump()
        self.name = self.getName(self.trumpVal)
        self.desc = self.getDesc(self.trumpVal)

    def randTrump(self):
        random.seed()
        trumpVal = random.randint(0,2)
        match trumpVal:
            case 0:
                trumpVal = 0
            case 1:
                trumpVal = 1
            case 2:
                trumpVal = 2
            case 3:
                trumpVal = -1
        return trumpVal
    
    def getName(self, trumpVal):
        match trumpVal:
            case 0:
                return "27"
            case 1:
                return "17"
            case 2:
                return "Refresh"
            
    def getDesc(self, trumpVal):
        match trumpVal:
            case 0:
                return "Increases the cap from 21 to 27"
            case 1:
                return "Decreases the cap from 21 to 17"
            case 2:
               return "Discards hand, draws 2 random cards and ends turn"
