

class Category:
    
  
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    
    def deposit(self, amount):
        self.amount += amount


    def withdraw(self, amount):
        self.amount -= amount

    
    
    def check_balance(self):
        print("Current balance in %s = " % self.category + str(self.amount))

    
    def transfer(self, category, amount):
        print("After transfer:")
        self.withdraw(amount)
        self.check_balance()
        category.deposit(amount)
        category.check_balance()

       
        
    

category_clothing = Category("Clothing", 200)
category_food = Category("Food", 300)
category_car = Category("Car", 200)
category_health = Category("Health", 250)

category_food.check_balance()
category_clothing.check_balance()
category_clothing.deposit(200)
category_clothing.check_balance()
category_clothing.withdraw(20)
category_clothing.check_balance()

category_clothing.transfer(category_food, 150)



