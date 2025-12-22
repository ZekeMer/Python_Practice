from resources import Inventory
from drink import maker
from money import register

# Todo: Using the previous lessons objectives, make another coffee machine except using the Classes already provided.
#*      Solution will start on line 100.





























































































# inventory = Inventory()        ## This is the common way of naming objects, by using lowercase format of the Class.
# cash = register()
# beverage = maker()

# on = True

# while on:
#     options = inventory.items()
#     customer_request = input(f"What would you like? ({options}): ").lower()
#     if customer_request == "off":
#         on = False
#     elif customer_request == "report":
#         beverage.report()
#         cash.report()
#     else:
#         drink = inventory.find_drink(customer_request)

#         if beverage.sufficient(drink) and cash.make_payment(drink.cost):
#             beverage.make_drink(drink)