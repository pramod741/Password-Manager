import tkinter
# from tkinter import END
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
import pandas


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, tkinter.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
        , 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # password=""
    # for char in range(1,nr_letters+1):
    #     password+=random.choice(letters)
    # for char in range(1,nr_symbols+1):
    #     password+=random.choice(symbols)
    # for char in range(1,nr_numbers+1):
    #     password+=random.choice(numbers)
    # print(password)

    # hardlevel
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)

    password1 = "".join(password_list)

    password_entry.insert(0, password1)
    pyperclip.copy(password1)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    mail = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": mail,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty")
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating the data
            data.update(new_data)

            with open("data.json", mode='w') as file:
                # saving th data
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #


def find_password():
    user_entry = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File Found")
    else:
        if user_entry in data:
            user_mail = data[user_entry]["email"]
            user_pass = data[user_entry]["password"]
            messagebox.showinfo(title=user_entry, message=f'Email: {user_mail}\nPassword: {user_pass}')
        else:
            messagebox.showinfo(title="Error", message=f"The {user_entry} details was not stored")

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canves = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file="logo.png")
canves.create_image(100, 100, image=image)
canves.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry

web_entry = tkinter.Entry(width=30)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_entry = tkinter.Entry(width=48)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'ppammi648@gmail.com')

password_entry = tkinter.Entry(width=30)
password_entry.grid(column=1, row=3)

# button

generate_button = tkinter.Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=41, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search = tkinter.Button(text="Search", width=14, command=find_password)
search.grid(column=2, row=1)

window.mainloop()
