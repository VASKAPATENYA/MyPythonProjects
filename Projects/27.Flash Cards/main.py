#region Libraries

from tkinter import *
import pandas
import random
import os

#endregion

#region Variables

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
path = "data/words_to_learn.csv"
isFile = os.path.isfile(path)
if(isFile == False):
    data = pandas.read_csv("data/french_words.csv")
else:
    data = pandas.read_csv("data/words_to_learn.csv")
to_learn = data.to_dict(orient="records")

#endregion

#region Functions

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_title, fill="black", text="French")
    canvas.itemconfig(card_word, fill="black", text=current_card["French"])
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])

def wrong_card():
    pass

def right_card():
    global current_card, isFile
    to_learn.remove(current_card)
    if(isFile == False):
        data1 = pandas.DataFrame(to_learn)
    data1.to_csv("data/words_to_learn.csv")
    

#endregion

#region UI

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=lambda: [next_card(), right_card()])
known_button.grid(row=1, column=1)

#endregion


next_card()
window.mainloop()
