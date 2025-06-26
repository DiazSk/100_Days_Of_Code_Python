from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    # Generate password with exactly 10 characters
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 3)
    nr_letters = 10 - nr_symbols - nr_numbers

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    # Clear existing password before inserting new one
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Check if the website or password is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    # Check if website already exists
    try:
        with open("password_manager.json", "r") as file:
            data = json.load(file)
            if website in data:
                messagebox.showinfo(title="Website Exists", 
                                  message=f"Password for {website} already exists!\n\nCurrent details:\nEmail: {data[website]['email']}\nPassword: {data[website]['password']}\n\nPlease use Search to find existing passwords.")
                return
    except FileNotFoundError:
        # File doesn't exist yet, so no duplicates possible
        data = {}
    except json.JSONDecodeError:
        # File is corrupted, start fresh
        data = {}

    # Ask the user if they want to save the password
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

    if is_ok:
        # Update data with new entry
        data.update(new_data)
        
        # Write updated data back to file
        with open("password_manager.json", "w") as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        email_entry.insert(0, "example@email.com")
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("password_manager.json", "r") as file:
            data = json.load(file)
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} \nPassword: {data[website]['password']}")
    except KeyError:
        messagebox.showinfo(title="Oops", message=f"No details for {website} exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=0)

# Logo
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, padx=(0, 20), pady=5, sticky="W")

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=3, sticky="EW", pady=5)
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, padx=(0, 20), pady=5, sticky="W")

# Buttons 
add_button = Button(text="Add", command=save_password, width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", pady=5)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="E", pady=5)

search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(column=2, row=1, sticky="E", pady=5)

window.mainloop()
