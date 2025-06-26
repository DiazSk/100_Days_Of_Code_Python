from menu import DEFAULT_RESOURCES

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        insufficient_resources = []
        
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                insufficient_resources.append(item)
                can_make = False
        
        if insufficient_resources:
            print("Sorry, there is not enough:", ", ".join(insufficient_resources))
            
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def refill_resources(self):
        """Refills the resources to the maximum capacity."""
        
        print("Current resource levels:")
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

        # Calculate and add the difference needed
        water_needed = DEFAULT_RESOURCES['water'] - self.resources['water']
        milk_needed = DEFAULT_RESOURCES['milk'] - self.resources['milk']
        coffee_needed = DEFAULT_RESOURCES['coffee'] - self.resources['coffee']

        if water_needed > 0:
            self.resources['water'] += water_needed
        if milk_needed > 0:
            self.resources['milk'] += milk_needed
        if coffee_needed > 0:
            self.resources['coffee'] += coffee_needed

        print("\nResources have been refilled:")
        print(f"Water: +{water_needed}ml (now {self.resources['water']}ml)")
        print(f"Milk: +{milk_needed}ml (now {self.resources['milk']}ml)")
        print(f"Coffee: +{coffee_needed}g (now {self.resources['coffee']}g)")

    def turn_off(self):
        """Turns off the coffee machine."""
        print("Turning off the coffee machine...")
        exit()

        
