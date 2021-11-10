from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPIN = 1234, custBalance = 10000):
        self.id = id
        self.custPIN = custPIN
        self.custBalance = custBalance

    def checkId(self):
        return self.id

    def checkPIN(self):
        return self.custPIN

    def checkBalance(self):
        return self.custBalance

    def withdraw(self, nominal):
        self.custBalance -= nominal

    def deposit(self, nominal):
        self.custBalance += nominal