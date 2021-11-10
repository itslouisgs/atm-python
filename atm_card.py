class ATMCard:
    def __init__(self, defaultPIN, defaultBalance):
        self.defaultPIN = defaultPIN
        self.defaultBalance = defaultBalance

    def checkDefaultPin(self):
        return self.defaultPIN
    
    def checkDefaultBalance(self):
        return self.defaultBalance