from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    u_input = website_entry.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            email = data[u_input]["email"]
            password = data[u_input]["password"]
            messagebox.showinfo(u_input, f"Email: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found")

    except KeyError:
        messagebox.showinfo("Error", "No details for the website exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for sym in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for num in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website.title(): {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        check = messagebox.askokcancel(title=website, message=f"These are the details entered \nEmail: {email}\n"
                                                      f"Password: {password}\nIs it okay to save?")
        if check:
            try:
                with open("data.json", mode="r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", mode="w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_pic)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()
website_button = Button(text="Search", command=find_password)
website_button.grid(column=2, row=1, sticky="EW")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "Isaac.cTD")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(width=36, text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
