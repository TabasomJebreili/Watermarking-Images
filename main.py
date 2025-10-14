from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title('Watermark Your Image')
window.minsize()

MAX_WIDTH = 600
MAX_HEIGHT = 500
img = Image.open('Aurora_history-b1c66fb.jpg')
img.thumbnail((MAX_WIDTH, MAX_HEIGHT))
w, h = img.size
photo = ImageTk.PhotoImage(img)

canvas = Canvas(width=w, height=h)
canvas.create_image(w//2, h//2, image=photo)
canvas.create_text(w//2, h//2, text='Insert text here', fill='white', font=('Ariel', 15, 'bold'))
canvas.grid(column=0, row=0, columnspan=2, rowspan=1)

label = Label(text="Insert text here")
label.grid(row=2, column=0)









window.mainloop()