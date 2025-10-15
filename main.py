from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
import tkinter.filedialog as fd
from tkinter import colorchooser


def path():
    root = fd.askopenfilename()
    return root


def save():
    global img
    save_address = fd.asksaveasfilename()
    if path:
        save_img = img.convert('RGB')
        save_img.save(address)


def rotate(direction):
    global img
    if direction == "right":
        img = img.rotate(90)
    if direction == "left":
        img = img.rotate(-90)
    return img


def new_text(fnt, size, x, y, text, r, g, b, a):
    global img
    transparent_img = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(transparent_img)
    font = ImageFont.truetype(fnt, size)
    draw.text((x, y), text, font=font, fill=(r, g, b, a))
    img = Image.alpha_composite(img, transparent_img)
    return img

def transparency(value):
    a = transparency_scale.get()
    return a

def choose_color():
    color, hex_code = colorchooser.askcolor(title='Choose the Color:')
    r = color[0]
    g = color[1]
    b = color[2]
    return r, g, b


window = Tk()
window.title('Watermark Your Image')
window.minsize()
window.configure(bg="black", pady=50, padx=50)

address = path()
img = Image.open(address).convert('RGBA')


select_file_button = (Button(text='Select image', bg="black", fg='white', font=('Helvetica', 12), command=path)
                      .grid(column=0, row=0, columnspan=2))

transparency_label = Label(text='transparency', fg='white', bg="black")
transparency_label.grid(column=0, row=1)
transparency_scale = Scale(from_=0, to=255)
transparency_scale.grid(column=1, row=1)










window.mainloop()