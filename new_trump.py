import random

class newTrumpCard:
    def __init__(self):
        self.trumpVal = self.randTrump()
        self.name = self.getName(self.trumpVal)
        self.desc = self.getDesc(self.trumpVal)

    def randTrump(self):
        random.seed()
        trumpVal = random.randint(0,1)
        match trumpVal:
            case 0:
                trumpVal = 0
            case 1:
                trumpVal = 1
            case 3:
                trumpVal = "Hearts"
            case 4:
                trumpVal = "Clubs"
        return trumpVal
    
    def getName(self, trumpVal):
        match trumpVal:
            case 0:
                return "27"
            case 1:
                return "17"
            
    def getDesc(self, trumpVal):
        match trumpVal:
            case 0:
                return "Increases the cap from 21 to 27"
            case 1:
                return "Decreases the cap from 21 to 17"
