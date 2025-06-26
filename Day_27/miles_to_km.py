from tkinter import *

# Calculate
def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


# Window
window = Tk()
window.title("Miles to Kilometers Converter")
window.geometry("400x200")
window.config(padx=20, pady=20)

# Labels
miles_label = Label(text="Miles", font=("Arial", 15))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 15))
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial", 15))
km_label.grid(column=2, row=1)

result_label = Label(text="0", font=("Arial", 15))
result_label.grid(column=1, row=1)

# Input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()