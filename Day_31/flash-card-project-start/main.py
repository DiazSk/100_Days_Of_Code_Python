from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import time


# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

WHITE = "#FFFFFF"
BLACK = "#000000"

# ---------------------------- DATA SETUP ------------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #
current_card = {}
flip_timer = None

def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    
    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="Completed!", fill=BLACK)
        canvas.itemconfig(card_word, text="All words learned!", fill=BLACK)
        canvas.itemconfig(card_background, image=card_front_img)
        return
    
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill=BLACK)
    canvas.itemconfig(card_word, text=current_card["French"], fill=BLACK)
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill=WHITE)
    canvas.itemconfig(card_word, text=current_card["English"], fill=WHITE)
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def dont_know():
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2, pady=50)

# Card Text
card_title = canvas.create_text(400, 150, text="", font=FONT_TITLE, fill=BLACK)
card_word = canvas.create_text(400, 263, text="", font=FONT_WORD, fill=BLACK)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=dont_know, bg=BACKGROUND_COLOR)
unknown_button.grid(row=1, column=0, pady=50)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known, bg=BACKGROUND_COLOR)
known_button.grid(row=1, column=1, pady=50)

next_card() # Start with a random card

window.mainloop()