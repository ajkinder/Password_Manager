# ---------------------------- IMPORTS ---------------------------- #
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print("generate button pressed.")  # For debugging purposes only.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    print("save button pressed.")  # For debugging purposes only.

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.config(padx=50, pady=50, background='black')

canvas = tk.Canvas(height=200, width=200)

# image = Image.open("logo.png")
# image = ImageTk.PhotoImage(image)

# img = Image.PhotoImage(file=image)
# logo_img = ImageTk.PhotoImage(Image.open("./logo.png"))
img = tk.PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website")
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
gerenate_password_button = tk.Button(text="Generate Password", bg='red', fg='white', command=generate_password)
gerenate_password_button.grid(row=3, column=2)
add_button = tk.Button(text="Add", width=36, bg='red', fg='white', command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
