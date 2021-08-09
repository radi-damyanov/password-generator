#!/usr/bin/env python3

from tkinter import *
import string 
import random
import pyperclip

# pass gen

password_chars = string.ascii_letters + string.digits + string.punctuation

def password_generator():
    password_field.delete(0, END)
    length = char_input.get()
    if (length.isdigit()) and (length > "0"):
        length = int(length)
        password = "".join([random.choice(password_chars) for _ in range(length)])
        password_field.insert(0, password)
        pyperclip.copy(password)
    else:
        password_field.insert(0, "Please enter a natural number!")

# UI

window = Tk()
window.title("Password Generator")
window.config(padx = 50, pady = 50, bg = "#383e56")

label_title = Label(text = "Password Generator",
    bg = "#383e56",
    fg = "#c5d7bd",
    font = ("Arial", 35, "bold"))

label_title.grid(row = 0, column = 0, columnspan = 3, pady = 30)

label_before_input = Label(text = "I want a password with",
    bg = "#383e56",
    fg = "#c5d7bd",
    font = ("Arial", 15, "bold"))

label_before_input.grid(row = 1, column = 0)

char_input = Entry(bg = "#999999", justify = CENTER, font = ("Arial", 10, "bold"))
char_input.grid(row = 1, column = 1)
char_input.insert(0, "12")
char_input.focus()

label_afrer_input = Label(text = "characters",
    bg = "#383e56",
    fg = "#c5d7bd",
    font = ("Arial", 15, "bold"))

label_afrer_input.grid(row = 1, column = 2)

generate_password_button = Button(text = "Generate Password & Copy to Clipboard",
    bg = "#00a13f",
    height = 4,
    width = 55,
    font = ("Arial", 10, "bold"),
    command = password_generator)

generate_password_button.grid(row = 2, column = 0, columnspan = 3, padx = 50, pady = 50)

password_field = Entry(bg = "#999999",
    font = ("Arial", 15, "bold"), 
    width = 40,
    justify = CENTER)

password_field.grid(row = 3, column = 0, columnspan = 3)

window.resizable(False, False)

window.mainloop()