from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")

to_learn = df.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(content_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card, image=card_front_img)
    flip_timer = window.after(3000, flipcard)


def flipcard():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(content_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=card_back_img)


def remove_card():
    to_learn.remove(current_card)
    next_card()


# ------------------------- UI ------------------------------------- #
window = Tk()
window.title("French Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flipcard)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
content_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, command=remove_card)
right_button.grid(row=1, column=0)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()



window.mainloop()

words_to_learn = pandas.DataFrame(to_learn)
words_to_learn.to_csv("./data/words_to_learn.csv", index=False)