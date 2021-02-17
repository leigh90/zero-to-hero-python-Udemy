class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'You have deposited Ksh{amount} and now have a balance of Ksh{self.balance}')
        return self.balance
    
    def withdraw(self, amount):

        if self.balance < amount:
            print(f'You cannot withdraw {amount} you have Ksh{self.balance} in your account')
            return self.balance
        else:
            self.balance -= amount
            print(f'You have withdrawn Ksh{amount} and now have a balance of Ksh{self.balance}')
            return self.balance

    
    def __str__(self):
        return f"{self.owner} \n {self.balance}"

accountone = Account('Ashley', 5000)
print(accountone)
print(accountone.owner)
print(accountone.balance)
accountone.deposit(50)
accountone.withdraw(6000)