from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True

while is_on:
    menu_items = menu.get_items()
    choice = input(f"What would you like? {menu_items} : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



# import turtle
# from turtle import Turtle , Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.color("red")
# timmy.shape("turtle")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)






















