from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(time_canvas, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    sb_sec = SHORT_BREAK_MIN * 60
    lb_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(lb_sec)
        title_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        countdown(sb_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(time_canvas, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        for n in range(math.floor(reps/2)):
            marks += "✔"
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)
tomato_png = PhotoImage(file="tomato.png")

title_label = Label(text="Timer", font=(FONT_NAME, 35, "normal"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

canvas = Canvas(width=300, height=316, bg=YELLOW, highlightthickness=0)
canvas.create_image(150, 158, image=tomato_png)
time_canvas = canvas.create_text(150, 178, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 15), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 15), command=reset)
reset_button.grid(row=2, column=2)

checkmark_label = Label(text="", font=(FONT_NAME, 15), bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=2, column=1)

window.mainloop()
