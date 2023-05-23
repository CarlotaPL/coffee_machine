from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
machine_on = True

while machine_on:
    user_choice = input(f"What would you like? ({menu.get_items()}):")
    if user_choice == "off":
        machine_on = False
        continue
    if user_choice == "report":
        coffee.report()
        money.report()
        continue
    if user_choice == "refill":
        coffee.add_resources()
        continue
    drink = menu.find_drink(user_choice)
    if drink == None:
        continue
    resources = coffee.is_resource_sufficient(drink)
    if resources == False:
        continue
    cost = money.make_payment(drink.cost)
    if cost == False:
        continue
    coffee.make_coffee(drink)






