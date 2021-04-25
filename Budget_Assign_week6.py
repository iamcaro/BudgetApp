import category

category_clothing = category.Category("Clothing", 200)
category_food = category.Category("Food", 300)
category_car = category.Category("Car", 200)
category_health = category.Category("Health", 250)

category_food.check_balance()
category_clothing.check_balance()
category_clothing.deposit(200)
category_clothing.check_balance()
category_clothing.withdraw(20)
category_clothing.check_balance()

category_clothing.transfer(category_food, 150)