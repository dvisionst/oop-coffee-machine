from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

keurig = CoffeeMaker()
coinstar = MoneyMachine()
drink_list = Menu()

using_coffee_machine = True
while using_coffee_machine:
    user_drink_choice = input(f'What would you like? {drink_list.get_items()}report/off: ')
    if user_drink_choice == 'off':
        using_coffee_machine = False
        break
    elif user_drink_choice == 'report':
        keurig.report()
        coinstar.report()
    elif drink_list.find_drink(user_drink_choice):
        bev_selected = drink_list.find_drink(user_drink_choice)
        if keurig.is_resource_sufficient(bev_selected):
            if coinstar.make_payment(bev_selected.cost):
                keurig.make_coffee(bev_selected)
