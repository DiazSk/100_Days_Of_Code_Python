import os
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        clear_screen()
        print("Welcome to the Coffee Machine!")
        print("Available commands for the coffee machine: report, refill, off")
        user_drink = input(f"What would you like? ({menu.get_items()}): ").lower()
        
        if user_drink == "off":
            coffee_maker.turn_off()
        elif user_drink == "report":
            coffee_maker.report()
            money_machine.report()
            input("\nPress Enter to continue for next order...").lower()
        elif user_drink == "refill":
            coffee_maker.refill_resources()
            input("\nPress Enter to continue for next order...").lower()
        else:
            drink = menu.find_drink(user_drink)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)
                        input("\nPress Enter to continue for next order...").lower()
                else:
                    input("\nPress Enter to continue for next order...").lower()

if __name__ == "__main__":
    main()
