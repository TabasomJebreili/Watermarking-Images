from tkinter import *
from PIL import Image, ImageTk
import random


def add_text():
    text_name = canvas.create_text(w // 2, h // 2, text='Write your text here', fill='white', font=('Courier New', 15, 'bold'))
    return text_name


window = Tk()
window.title('Watermark Your Image')
window.minsize()
window.configure(bg="black", pady=50, padx=50)

MAX_WIDTH = 600
MAX_HEIGHT = 500
img = Image.open('Aurora_history-b1c66fb.jpg')
img.thumbnail((MAX_WIDTH, MAX_HEIGHT))
w, h = img.size
photo = ImageTk.PhotoImage(img)

canvas = Canvas(width=w, height=h, bg='black', highlightthickness=0)
canvas.create_image(w//2, h//2, image=photo)
canvas.grid(column=0, row=0, columnspan=2, rowspan=1)

x_label = Label(text="Insert the x position of your text:", bg='black', fg="white", font=('Courier New', 12))
x_label.grid(column=0, columnspan=1, row=2, sticky="w")

x_place = Entry(width=8, bg='white', fg='black', font=('Courier New', 10))
x_place.insert(END, 'e.g. 120')
x_place.grid(column=1, row=2, sticky="w")

y_label = Label(text="Insert the y position of your text:", bg='black', fg="white", font=('Courier New', 12))
y_label.grid(column=0, columnspan=1, row=3, sticky="w")

y_place = Entry(width=8, bg='white', fg='black', font=('Courier New', 10))
y_place.insert(END, 'e.g. 120')
y_place.grid(column=1, row=3, sticky="w")

your_text_label = Label(text="Insert the text:", bg='black', fg="white", font=('Courier New', 12))
your_text_label.grid(column=0, columnspan=1, row=4, sticky="w")

your_text_entry = Entry(width=15, bg='white', fg='black', font=('Courier New', 10))
your_text_entry.insert(END, 'Write your text here')
your_text_entry.grid(column=1, columnspan=1, row=4, sticky="w")

color_label = Label(text='Choose the color of your text:', bg='black', fg="white", font=('Courier New', 12))
color_label.grid(column=0, columnspan=1, row=5, sticky="w")



add_text_button = Button(text='Add Text', bg='black', fg='white', command=add_text, font=('Courier New', 14))
add_text_button.config(pady=20)
add_text_button.grid(column=0, row=6)









window.mainloop()