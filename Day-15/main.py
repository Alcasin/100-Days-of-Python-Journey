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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MACHINE_MONEY =  0.0

def format_resources(item):
    item_count = resources[item]
    return item_count

def report():
    print(f" Water: {format_resources("water")}ml  ")
    print(f" Milk: {format_resources("milk")}ml  ")
    print(f" Coffee: {format_resources("coffee")}g  ")
    print(f" Money: ${MACHINE_MONEY}  ")

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total
machine = True
while machine:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        machine = False
    elif choice == "report":
        report()
    else:
        if choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                money = process_coins()
                if money < MENU[choice]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    if money > MENU[choice]["cost"]:
                        offer = money - MENU[choice]["cost"]
                        offer = round(offer,2)
                        print(f"Here is ${offer} dollars in change.")
                    print(f"Here is your {choice}. Enjoy!")

                    for item in drink["ingredients"] :
                        resources[item] -= MENU[choice]["ingredients"][item]
                    MACHINE_MONEY += MENU[choice]["cost"]


        else:
            print("Invalid selection, please try again.")


