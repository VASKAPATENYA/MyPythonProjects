import random
import pyperclip
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")
    pyperclip.copy(password)

    psw_entry.delete(0, END)
    psw_entry.insert(0, string=f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    with open("psw_file.txt", "a") as data:
        data.write(f"{web_entry.get()} | {mail_entry.get()} | {psw_entry.get()}\n")
    messagebox.showinfo("Successful", "Password Saved!")
    web_entry.delete(0, END)
    psw_entry.delete(0, END)
    web_entry.focus()

# region UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="gray")

logo_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.config(bg="gray", highlightthickness=0)
canvas.grid(row=0, column=1)

# Label

web_label = Label(text="Web Site:")
web_label.config(bg="gray")
web_label.grid(row=1, column=0)

mail_label = Label(text="Email/Username:")
mail_label.config(bg="gray")
mail_label.grid(row=2, column=0)

psw_label = Label(text="Password:")
psw_label.config(bg="gray")
psw_label.grid(row=3, column=0)

# Entry

web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

mail_entry = Entry(width=35)
mail_entry.insert(0,string="alibr366@gmail.com")
mail_entry.grid(row=2, column=1, columnspan=2)

psw_entry = Entry(width=17)
psw_entry.grid(row=3, column=1)


# Button

generate_btn = Button(text="Generate Password", command=generate)
generate_btn.config(bg="gray", highlightthickness=0)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=30, command=add)
add_btn.config(bg="gray", highlightthickness=0)
add_btn.grid(row=4, column=1, columnspan=2)

# endregion

window.mainloop()