# from turtle import Turtle, Screen

# my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("chartreuse")
# my_turtle.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Houses of Hogwarts", ["Ravenclaw", "Hufflepuff","Gryffindor","Slytherin"])
# print(table)

# table2 = PrettyTable()
# table2.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table2.add_column("Type", ["Electric", "Water", "Fire"])
# table2.align = "r"
# print(table2)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

def main():
    selection = input(f"What would you like? ({my_menu.get_items()}): ")

    if selection != "off":
        if selection == "report":
            my_coffee_maker.report()
            my_money_machine.report()
        elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
            selected_coffee = my_menu.find_drink(selection)

            if my_coffee_maker.is_resource_sufficient(selected_coffee):
                if my_money_machine.make_payment(selected_coffee.cost):
                    my_coffee_maker.make_coffee(selected_coffee)
        
        main()
                   
main()        