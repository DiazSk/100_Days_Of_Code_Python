import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

try:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    
    # Validate input ranges
    if nr_letters < 0 or nr_symbols < 0 or nr_numbers < 0:
        print("Please enter non-negative numbers only.")
        exit()
    
    if nr_letters + nr_symbols + nr_numbers == 0:
        print("Password must have at least one character.")
        exit()

    # Easy Level - Order not randomised:
    password = ""
    for char in range(nr_letters):
        password += random.choice(letters)

    for char in range(nr_symbols):
        password += random.choice(symbols)

    for char in range(nr_numbers):
        password += random.choice(numbers)

    print(f"\nYour password in easy level is: {password}")

    # Hard Level - Order of characters randomised:
    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = "".join(password_list)  # More efficient than concatenation in loop

    print(f"Your password in hard level is: {password}")

except ValueError:
    print("Please enter valid numbers only.")
except KeyboardInterrupt:
    print("\nPassword generation cancelled.")
