import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import messagebox

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
loop = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(textimage, text="00:00")
    checkmark.config(text="")
    global loop
    loop = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(limit):
    minu = math.floor(limit / 60)
    sec = limit % 60
    if sec < 10:
        sec = "0" + str(sec)
    canvas.itemconfig(textimage, text=f"{minu}:{sec}")
    if limit > 0:
        global timer
        timer = window.after(1000, count_down, limit - 1)
    else:
        start_timer()
        if loop % 7 == 0:
            checkmark.config(text="✔✔✔✔")
        elif loop % 5 == 0:
            checkmark.config(text="✔✔✔")
        elif loop % 3 == 0:
            checkmark.config(text="✔✔")
        else:
            checkmark.config(text="✔")


def start_timer():
    global loop
    loop += 1
    work_timing = 60 * WORK_MIN
    short_break_timing = 60 * SHORT_BREAK_MIN
    long_break_timing = 60 * LONG_BREAK_MIN
    if loop % 8 == 0:
        count_down(long_break_timing)
        label.config(text="BREAK", fg=RED)
        window.attributes('-topmost', 1)
        messagebox.showinfo("Message", "20 minutes of break")
        window.attributes('-topmost', 0)
    elif loop % 2 == 0:
        count_down(short_break_timing)
        label.config(text="BREAK", fg=PINK)
        window.attributes('-topmost', 1)
        messagebox.showinfo("BREAK", "5 minutes of break")
        window.attributes('-topmost', 0)
    else:
        count_down(work_timing)
        label.config(text="WORK", fg=GREEN)
        if loop != 1:
            window.attributes('-topmost', 1)
            messagebox.showinfo("WORK", "Time to work!")
            window.attributes('-topmost', 0)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro timer")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=230, height=240, bg=YELLOW, highlightthickness=0)
photoimage = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(125, 120, image=photoimage, )
textimage = canvas.create_text(120, 140, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=2, row=2)

label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label.grid(column=2, row=1)
checkmark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "normal"))
checkmark.grid(column=2, row=4)
start_button = tkinter.Button(text="start", padx=5, pady=5, highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)
reset_button = tkinter.Button(text="reset", padx=5, pady=5, highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

window.mainloop()
