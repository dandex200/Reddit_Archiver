#   ▄████████    ▄████████ ████████▄  ████████▄   ▄█      ███             ▄████████    ▄████████  ▄████████    ▄█    █▄     ▄█   ▄█    █▄     ▄████████    ▄████████
#   ███    ███   ███    ███ ███   ▀███ ███   ▀███ ███  ▀█████████▄        ███    ███   ███    ███ ███    ███   ███    ███   ███  ███    ███   ███    ███   ███    ███
#   ███    ███   ███    █▀  ███    ███ ███    ███ ███▌    ▀███▀▀██        ███    ███   ███    ███ ███    █▀    ███    ███   ███▌ ███    ███   ███    █▀    ███    ███
#  ▄███▄▄▄▄██▀  ▄███▄▄▄     ███    ███ ███    ███ ███▌     ███   ▀        ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄ ███▌ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀
# ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███    ███ ███    ███ ███▌     ███          ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀  ███▌ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
# ▀███████████   ███    █▄  ███    ███ ███    ███ ███      ███            ███    ███ ▀███████████ ███    █▄    ███    ███   ███  ███    ███   ███    █▄  ▀███████████
#   ███    ███   ███    ███ ███   ▄███ ███   ▄███ ███      ███            ███    ███   ███    ███ ███    ███   ███    ███   ███  ███    ███   ███    ███   ███    ███
#   ███    ███   ██████████ ████████▀  ████████▀  █▀      ▄████▀          ███    █▀    ███    ███ ████████▀    ███    █▀    █▀    ▀██████▀    ██████████   ███    ███
#   ███    ███                                                                         ███    ███                                                          ███    ███


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Root Window
root = tk.Tk()
width = 1200
height = 600
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
root.title("REDDIT-ARCHIVER")

# GUI Variables
reddit_username = tk.StringVar()

# GUI Design
title_label = ttk.Label(root, text='logo')
title_label.place(x=100, y=5, width=1200, height=500)

username_label = ttk.Label(root, text="Reddit Username: ")
username_label.place(x=60, y=500, width=200, height=30)

username_entry = ttk.Entry(root, textvariable=reddit_username)
username_entry.place(x=250, y=530, width=200, height=30)

# Initialize GUI
root.mainloop()


# URL Configuration
url = 'https://old.reddit.com/user/'
url_final = url + reddit_username.get()

# WebDriver Initialization
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url_final)

title_list = driver.find_elements_by_class_name("title")

for i in title_list:
    print("Title " + i.text)
