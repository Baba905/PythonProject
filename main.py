BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
from random import choice

word_to_learn = {}
chosen_word = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    word_to_learn = data.to_dict(orient="records")
else:
    word_to_learn = data.to_dict(orient="records")

# ----------------------------------- PICK WORD ------------------------------------------ #


def next_card():
    global chosen_word,flip_timer
    window.after_cancel(flip_timer)
    chosen_word = choice(word_to_learn)
    flash_card.itemconfig(language, text="English", fill="black")
    flash_card.itemconfig(word, text=chosen_word["English"], fill="black")
    flash_card.itemconfig(background_image, image=flash_card_image_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    flash_card.itemconfig(language, text="French", fill="white")
    flash_card.itemconfig(word, text=chosen_word["French"], fill="white")
    flash_card.itemconfig(background_image, image=flash_card_image_back)


def is_known():
    word_to_learn.remove(chosen_word)
    new_data= pd.DataFrame(word_to_learn)
    new_data.to_csv("data/words_to_learn.csv",index=False)
    next_card()
# ----------------------------------- UI SETUP ------------------------------------------- #

window = Tk()
window.minsize(width=900, height=600)
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func= flip_card)
# Flash Card

flash_card = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
flash_card_image_front = PhotoImage(file='images/card_front.png')
flash_card_image_back = PhotoImage(file='images/card_back.png')
background_image = flash_card.create_image(400,263,image= flash_card_image_front)
language = flash_card.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word = flash_card.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
flash_card.grid(column=0,row=0, columnspan=2)




# Right Button
right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1,row=1)
right_button["command"] = is_known

#Wrong Button
wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)
wrong_button["command"] = next_card


next_card()
window.mainloop()