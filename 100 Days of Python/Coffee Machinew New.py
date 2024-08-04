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

# check whether coffee machine has sufficient ingredients to make coffee
def isResourceSufficient(ingredients):
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Not enough {ingredient}")
            return False
    return True

def totalCoins():
    print("Please insert coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def successfulTransaction(money, price):
    if money >= price:
        change = round(money - price, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += price
        return True
    else:
        print("Not enough money")
        return False
    
def makeCoffee(coffeeType, ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print("Here is your {coffeeType}")

is_on = True
while is_on == True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if isResourceSufficient(drink["ingredients"]):
            payment = totalCoins()
            if successfulTransaction(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])