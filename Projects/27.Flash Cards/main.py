import timeeee
import random
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
on = True

# region Data

data = pandas.read_csv("data/data.csv")
to_learn = data.to_dict(orient="records")


# endregion

# region Functions

def nextCard():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"].upper())

def flipCard():
    card_back_img = PhotoImage(file="images/card_back.png")
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, fill="white")
    canvas.itemconfig(card_word, fill="white")

# endregion

# region Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#endregion

# region Canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# endregion

# region Buttons
cross_img=PhotoImage(file="images/wrong.png")
unknown_btn=Button(image=cross_img, command=nextCard)
unknown_btn.config(bg=BACKGROUND_COLOR, highlightthickness=0)
unknown_btn.grid(row=1, column=0)

right_img=PhotoImage(file="images/right.png")
known_btn=Button(image=right_img, command=nextCard)
known_btn.config(bg=BACKGROUND_COLOR, highlightthickness=0)
known_btn.grid(row=1, column=1)

# endregion

    
nextCard()

window.mainloop()