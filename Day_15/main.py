import os

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

# Default resource levels
DEFAULT_RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

resources = DEFAULT_RESOURCES.copy()

# TODO: 4. Check if resources are sufficient for the order.
def check_resources(user_drink):
    if user_drink == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        if resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        return True

    if user_drink == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            return False
        return True

    if user_drink == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            return False
        return True


# TODO: 2. Turn off the machine.
def turn_off(user_drink):
    if user_drink == "off":
        print("Turning off the machine...")
        exit()


# TODO: 3. Print report of resources.
def print_report(user_drink):
    if user_drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")


# TODO: 5. Process coins. Check if resources are sufficient and calculate change. Update resources and add profit.
def process_coins(user_drink):
    if user_drink not in MENU:
        return
    
    if not check_resources(user_drink):
        return
    
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    cost = MENU[user_drink]["cost"]
    
    if total >= cost:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
        
        # Make the coffee and update resources
        make_coffee(user_drink)
        resources["money"] += cost
    else:
        print("Sorry, that's not enough money. Money refunded.")


# TODO: 6. Make coffee.
def make_coffee(user_drink):
    """Deduct the required ingredients from the resources."""
    for ingredient, amount in MENU[user_drink]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {user_drink} ☕. Enjoy!")

# TODO: 7. Refill resources.
def refill_resources():
    """Refill resources to their default levels, only adding what's needed."""
    global resources
    print("Current resource levels:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    
    # Calculate and add the difference needed
    water_needed = DEFAULT_RESOURCES['water'] - resources['water']
    milk_needed = DEFAULT_RESOURCES['milk'] - resources['milk']
    coffee_needed = DEFAULT_RESOURCES['coffee'] - resources['coffee']
    
    if water_needed > 0:
        resources['water'] += water_needed
    if milk_needed > 0:
        resources['milk'] += milk_needed
    if coffee_needed > 0:
        resources['coffee'] += coffee_needed
    
    print("\nResources have been refilled:")
    print(f"Water: +{water_needed}ml (now {resources['water']}ml)")
    print(f"Milk: +{milk_needed}ml (now {resources['milk']}ml)")
    print(f"Coffee: +{coffee_needed}g (now {resources['coffee']}g)")


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


# TODO: 1. Main program loop
def main():
    while True:
        # Clear screen and show prompt
        clear_screen()
        print("Welcome to the Coffee Machine!")
        print("Available commands: espresso, latte, cappuccino, report, refill, off")
        user_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if user_drink == "off":
            turn_off(user_drink)
        elif user_drink == "report":
            print_report(user_drink)
            input("\nPress Enter to continue for next order...").lower()
        elif user_drink == "refill":
            refill_resources()
            input("\nPress Enter to continue for next order...").lower()
        else:
            process_coins(user_drink)
            input("\nPress Enter to continue for next order...").lower()


if __name__ == "__main__":
    main()
