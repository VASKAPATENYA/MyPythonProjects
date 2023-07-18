from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=300, height=300)


label=Label(text="I Am A Label", font=("Arial", 18, "bold"))
label.grid(column=0, row=0)

button=Button(text="Click Me!")
button.grid(column=1, row=1)

input=Entry(width=10)
input.grid(column=3, row=2)

new_label=Label(text="New Label", font=("Arial", 18, "bold"))
new_label.grid(column=3, row=0)
window.mainloop()