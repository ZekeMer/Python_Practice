
#! Coffee Machine
# Todo: Ask user what the Customer wants to drink.
# Todo: Have an On and Off function for the Coffee machine.
# Todo: Printable report of materials at start of shift.
# Todo: Evaluate resources to make coffee.
# Todo: Have a way to process differernt coins
# Todo: Have a way to deal with Customer who does not have the correct amount in coins.
# Todo: Be able to check all transactions. (With ability to return correct coins if insufficent amount.)
# Todo: If Customer has correct amount, have a way to add the correct amount to printable resources as profit.
# Todo: Have Printable resource list, That shows what you are currently at. (Profit should be at $0.00 for start of shift)
# Todo: Ensure there is enough resources to make the Customers coffee and deduct resources used from resources left.
# Todo: Give Customer there coffee and give them a farewell.
#*      Solution starts on line 100.

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}



























































# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# def sufficient(drink_ingredients):              # Returns true if sufficent resources, else false
#     for item in drink_ingredients:
#         if drink_ingredients[item] >= resources[item]:
#             print(f"Not enough {item}, go to back of the line.")
#             return False
#     return True

# def coins():                                    # Returns Value of coins inserted.
#     print("Please insert coins!")
#     total = int(input("how many quarters? ")) * 0.25
#     total += int(input("how many dimes? ")) * 0.10
#     total += int(input("how many nickels? ")) * 0.05
#     total += int(input("how many pennies? ")) * 0.01
#     return total

# def correct_amount(received, cost):                 # Retun true if payment is accepted
#     if received >= cost:
#         change = round(received - cost, 2)
#         print(f"Here is your change of ${change}.\n 'How does anyone overpay when they are paying in coins'🙄 ")
#         global profit
#         profit += cost
#         return True
#     else:
#         print("insufficient money, stop wasting our time!🤬\n 'coins are thrown at customer'")
#         return False
# def make(drink_name, order_ingre):
#     for item in order_ingre:
#         resources[item] -= order_ingre[item]
#     print(f"Here is your {drink_name}")
# on = True

# while on:
#     customer_request = input("What would you like? 'espresso', 'latte', or 'cappuccino': ")
#     if customer_request == "off":
#         on = False
#     elif customer_request == "report":
#         print(f"Water: {resources['water']} ml")
#         print(f"Milk: {resources['milk']}ml") 
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = menu[customer_request]
#         if sufficient(drink["ingredients"]):
#             payment = coins()
#             if correct_amount(payment, drink["cost"]):
#                 make(customer_request, drink["ingredients"])