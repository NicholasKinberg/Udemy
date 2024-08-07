# Coffee machine
# What would you like? espresso, latte, or cappuccino
# Water: 300ml
# Coffee: 100g
# Money: $0
# Prompt: Please insert coins
# How many quarters?
# How many dimes?
# How many nickles?
# How many pennies?
# Here is x in change.
# Here is your latte. Enjoy!
# espressoDict = {"type": "espresso", "price": 1.50, "water": 50, "coffee": 18, "milk": 0}
# latteDict = {"type": "latte", "price": 2.50, "water": 200, "coffee": 24, "milk": 150}
# cappuccinoDict = {"type": "cappuccino", "price": 3.00, "water": 250, "coffee": 24, "milk": 100}
# class CoffeeMachine():
#     def __init__(self, coffeeType, water, coffee, money):
#         self.coffeeType = coffeeType
#         self.water = water
#         self.coffee = coffee
#         self.money = money
    
#     def whatWouldYouLike(self, coffeeType):
#         coffeeType = input("What coffee would you like? (espresso, latte, or cappuccino): ")


MENU = {
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
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])