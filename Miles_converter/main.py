from tkinter import *

FONT = ("Arial", 10, "normal")


def button_clicked():
    user_input = float(input.get())
    km_output = user_input * 1.60934
    km_num.config(text=f"{km_output:.2f}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

input = Entry(width=15)
input.grid(column=1, row=0)

miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)
miles.config(padx=3, pady=3)

label = Label(text="is equal to", font=FONT)
label.grid(column=0, row=1)

km_num = Label(text="0", font=FONT)
km_num.grid(column=1, row=1)

km = Label(text="Km", font=FONT)
km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()