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

# Prompt user by asking “​What would you like? (espresso/latte/cappuccino):”​
# Turn off the Coffee Machine by entering “​off”​ to the prompt.
# Print report.
# Check resources sufficient?
# Process coins.
# Check transaction successful?
# Make Coffee.
def totalCoin():
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01

def resourcesSufficient(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print("Not enough {ingredient}")
            return False
    return True

def transactionSuccessful(money, price):
    if money >= price:
        global profit
        profit += price
        change = round(money - price, 2)
        return change
    return False

def makeCoffee(coffeeType, ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print("here is your {coffeeType}")

is_on = True
while is_on == True:
    choice = input("What kind of coffee do you want? (espresso, latte, cappuccino): ")
    if choice == "off":
        is_on = False
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resourcesSufficient(drink["ingredients"]):
            payment = totalCoin()
            if transactionSuccessful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee = CoffeeMaker()
report = coffee.report()
resourceSufficient = coffee.is_resource_sufficient()
madeCoffee = coffee.make_coffee()

items = Menu()
getItems = items.get_items()
order = items.find_drink("cappuccino")

money = MoneyMachine()
report = money.report()
numberOfCoins = money.process_coins()
payment = money.make_payment()