#!/usr/bin/env python3

from variables import *
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

def symbols_button():
    global password_chars
    global n_button_count
    global s_button_count
    s_button_count += 1

    if s_button_count % 2 != 0:
        toggle_symbols_button.config(bg = green_button)
        password_chars = password_chars + string.punctuation
    
    else:
        toggle_symbols_button.config(bg = red_button)
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
        toggle_numbers_button.config(bg = green_button)
        password_chars = password_chars + string.digits
    
    else:
        toggle_numbers_button.config(bg = red_button)
        if s_button_count % 2 != 0:
            password_chars = string.ascii_letters + string.punctuation
        
        else:
            password_chars = string.ascii_letters

# theme switcher function

def theme_button():
    global t_button_count
    t_button_count += 1

    if t_button_count % 2 == 0:
        window.config(bg = nightmode_color)

        label_title.config(bg = nightmode_color, fg = nightmode_text)

        label_before_input.config(bg = nightmode_color, fg = nightmode_text)

        label_afrer_input.config(bg = nightmode_color, fg = nightmode_text)

        generate_password_button.config(bg = nightmode_button)

        theme_switch_button.config(text = "☀️", bg = nightmode_button)

    else:
        window.config(bg = lightmode_color)

        label_title.config(bg = lightmode_color, fg = lightmode_text)

        label_before_input.config(bg = lightmode_color, fg = lightmode_text)

        label_afrer_input.config(bg = lightmode_color, fg = lightmode_text)

        generate_password_button.config(bg = lightmode_button, fg = lightmode_text)

        theme_switch_button.config(text = "🌒", bg = lightmode_button)

# UI

window = Tk()
window.title("Password Generator")
window.config(padx = 50, pady = 50, bg = nightmode_color)

label_title = Label(text = "Password Generator",
    bg = nightmode_color,
    fg = nightmode_text,
    font = (font, 35, "bold"))

label_title.grid(row = 0, column = 0, columnspan = 3, pady = 30)

label_before_input = Label(text = "I want a password with",
    bg = nightmode_color,
    fg = nightmode_text,
    font = (font, 15, "bold"))

label_before_input.grid(row = 1, column = 0)

char_input = Entry(bg = input_field_color, justify = CENTER, font = (font, 10, "bold"))
char_input.grid(row = 1, column = 1)
char_input.insert(0, "12")
char_input.focus()

label_afrer_input = Label(text = "characters",
    bg = nightmode_color,
    fg = nightmode_text,
    font = (font, 15, "bold"))

label_afrer_input.grid(row = 1, column = 2)

generate_password_button = Button(text = "Generate Password & Copy to Clipboard",
    bg = nightmode_button,
    height = 4,
    width = 55,
    font = (font, 10, "bold"),
    command = password_generator)

generate_password_button.grid(row = 2, column = 0, columnspan = 3, padx = 50, pady = 50)

password_field = Entry(bg = input_field_color,
    font = (font, 15, "bold"), 
    width = 40,
    justify = CENTER)

password_field.grid(row = 3, column = 0, columnspan = 3)

theme_switch_button = Button(text = "☀️",
    bg = nightmode_button,
    height = 1,
    width = 5,
    font = (font, 15, "bold"),
    command = theme_button,
    justify = CENTER)

theme_switch_button.grid(row = 4, column = 0, pady = 50)

toggle_symbols_button = Button(text = "Symbols",
    bg = red_button,
    height = 1, 
    width = 6,
    font = (font, 15, "bold"),
    command = symbols_button,
    justify = CENTER)

toggle_symbols_button.grid(row = 4, column = 1, pady = 50)

toggle_numbers_button = Button(text = "Numbers",
    bg = red_button,
    height = 1, 
    width = 6,
    font = (font, 15, "bold"),
    command = numbers_button,
    justify = CENTER)

toggle_numbers_button.grid(row = 4, column = 2, pady = 50)

window.resizable(False, False)

window.mainloop()