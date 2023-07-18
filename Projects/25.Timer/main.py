from tkinter import *
from playsound import *
import time
import math


# region CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer=None
reps=0
marks=""

# endregion

# region TIMER RESET 
def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    chck_label.config(text="")
    global marks
    global reps
    marks=""
    reps=0
# endregion

# region TIMER MECHANISM 
def startTimer():
    global reps
    reps+=1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text="Break", fg=RED)
        countdown(long_sec)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        countdown(short_sec)
    else:
        title.config(text="Work", fg=GREEN)
        countdown(work_sec)
        
    
# endregion

# region COUNTDOWN MECHANISM 
def countdown(count):
    global marks
    count_min = math.floor(count / 60)
    count_sec= count % 60
    if int(count_sec)<10:
        count_sec=f"0{count_sec}"
    if count_min<10:
        count_min=f"0{count_min}"

    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000, countdown, count - 1)
    else:
        startTimer()
        
        if reps % 2 == 0:
            marks+="✔"
            chck_label.config(text=marks)

        # marks=""
        # work_sessions=math.floor(reps/2)
        # for _ in range(work_sessions):
        #     marks+="✔"
        #     chck_label.config(text=marks)

# endregion

# region UI SETUP
window = Tk()
window.title("Timer")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img=PhotoImage(file="tomato.png")

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas_text=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


title=Label(text="Timer", font=(FONT_NAME, 40, "bold"))
title.config(foreground=GREEN, background=YELLOW)
title.grid(row=0, column=1)


start_btn=Button(text="Start", command=startTimer)
start_btn.grid(row=2, column=0)

chck_label=Label(fg=GREEN, font=("bold"))
chck_label.config(bg=YELLOW)
chck_label.grid(row=3, column=1)


reset_btn=Button(text="Reset", command=resetTimer)
reset_btn.grid(row=2, column=2)


window.mainloop()

# endregion