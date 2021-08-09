#!/usr/bin/env python3

from tkinter import *
import string 
import random
import pyperclip

# pass gen function

password_chars = string.ascii_letters

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

# button functions

s_button_count = 0
n_button_count = 0

def symbols_button():
    global password_chars
    global n_button_count
    global s_button_count
    s_button_count += 1

    if s_button_count % 2 != 0:
        toggle_symbols_button.config(bg = "#00d100")
        password_chars = password_chars + string.punctuation
    
    else:
        toggle_symbols_button.config(bg = "#ff3e30")
        if n_button_count % 2 != 0:
            password_chars = string.ascii_letters + string.digits
        
        else:
            password_chars = string.ascii_letters

def numbers_button():
    global password_chars
    global s_button_count
    global n_button_count

    n_button_count += 1

    if n_button_count % 2 != 0:
        toggle_numbers_button.config(bg = "#00d100")
        password_chars = password_chars + string.digits
    
    else:
        toggle_numbers_button.config(bg = "#ff3e30")
        if s_button_count % 2 != 0:
            password_chars = string.ascii_letters + string.punctuation
        
        else:
            password_chars = string.ascii_letters

# theme switcher function

i = 0

def theme_button():
    global i
    i += 1

    if i % 2 == 0:
        nightmode_color = "#222222"
        nightmode_text = "#c5d7bd"
        nightmode_button = "#4169e1"

        window.config(bg = nightmode_color)

        label_title.config(bg = nightmode_color, fg = nightmode_text)

        label_before_input.config(bg = nightmode_color, fg = nightmode_text)

        label_afrer_input.config(bg = nightmode_color, fg = nightmode_text)

        generate_password_button.config(bg = nightmode_button)

        theme_switch_button.config(text = "☀️", bg = nightmode_button)

    else:
        lightmode_color = "#DEE4E7"
        lightmode_text = "#000000"
        lightmode_button = "#7cbcff"

        window.config(bg = lightmode_color)

        label_title.config(bg = lightmode_color, fg = lightmode_text)

        label_before_input.config(bg = lightmode_color, fg = lightmode_text)

        label_afrer_input.config(bg = lightmode_color, fg = lightmode_text)

        generate_password_button.config(bg = lightmode_button, fg = lightmode_text)

        theme_switch_button.config(text = "🌒", bg = lightmode_button)

# UI

window = Tk()
window.title("Password Generator")
window.config(padx = 50, pady = 50, bg = "#222222")

label_title = Label(text = "Password Generator",
    bg = "#222222",
    fg = "#c5d7bd",
    font = ("Arial", 35, "bold"))

label_title.grid(row = 0, column = 0, columnspan = 3, pady = 30)

label_before_input = Label(text = "I want a password with",
    bg = "#222222",
    fg = "#c5d7bd",
    font = ("Arial", 15, "bold"))

label_before_input.grid(row = 1, column = 0)

char_input = Entry(bg = "#999999", justify = CENTER, font = ("Arial", 10, "bold"))
char_input.grid(row = 1, column = 1)
char_input.insert(0, "12")
char_input.focus()

label_afrer_input = Label(text = "characters",
    bg = "#222222",
    fg = "#c5d7bd",
    font = ("Arial", 15, "bold"))

label_afrer_input.grid(row = 1, column = 2)

generate_password_button = Button(text = "Generate Password & Copy to Clipboard",
    bg = "#4169e1",
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

theme_switch_button = Button(text = "☀️",
    bg = "#4169e1",
    height = 1,
    width = 5,
    font = ("Arial", 15, "bold"),
    command = theme_button,
    justify = CENTER)

theme_switch_button.grid(row = 4, column = 0, pady = 50)

toggle_symbols_button = Button(text = "Symbols",
    bg = "#ff3e30",
    height = 1, 
    width = 6,
    font = ("Arial", 15, "bold"),
    command = symbols_button,
    justify = CENTER)

toggle_symbols_button.grid(row = 4, column = 1, pady = 50)

toggle_numbers_button = Button(text = "Numbers",
    bg = "#ff3e30",
    height = 1, 
    width = 6,
    font = ("Arial", 15, "bold"),
    command = numbers_button,
    justify = CENTER)

toggle_numbers_button.grid(row = 4, column = 2, pady = 50)

window.resizable(False, False)

window.mainloop()