class Category:
    
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount -= amount

    def check_balance(self):
        print("Current balance in %s = %d" % (self.category, self.amount))

    def transfer(self, category, amount):
        print("Balances after transfer:")
        self.withdraw(amount)
        self.check_balance()
        category.deposit(amount)
        category.check_balance()

