from tkinter import *



def calculate():
    mile=input.get()
    km=float(mile) * 1.6
    label_oc.config(text=int(km))






# Window
window=Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=100)
window.config(padx=25, pady=25)

# Entry
input=Entry(width=10)
input.insert(END, string="0")
input.grid(row=0, column=1)
input.focus()


# Label "is equal to"
label_eq=Label(text="is equal to")
label_eq.grid(row=1, column=0)

# Label Outcome
label_oc=Label(text="0")
label_oc.grid(row=1, column=1)

# Label Miles
label_m=Label(text="Miles")
label_m.grid(row=0, column=2)

# Label Km
label_km=Label(text="Km")
label_km.grid(row=1, column=2)


# Button
button=Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)


window.mainloop()