class Bankaccount:
    def innit__(self, balance=0):
        
        balance = self.balance
    def deposit(self, deposit):
        if deposit > 0:
            return self.balance += deposit
        else:
            return False
    def withdrawal(self, withdrawal):
        if withdrawal > self.balance:
            return False
 #           return "Can't withdraw more than balance"
        self.balance -= withdrawal
        return True
         