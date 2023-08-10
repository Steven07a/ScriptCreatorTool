
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from functions import script_functions
from PIL import Image

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\steve\OneDrive\Desktop\tkinter folder\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def update_screenshot(img_path):    
    photo_image = script_functions.take_screenshot(img_path)
    img = Image.open("test.png")
    img = img.resize((525,609))
    img.save("test.png")

    new_image = PhotoImage(file="test.png")
    canvas.itemconfig(image_2, image=new_image)

window = Tk()

window.geometry("1201x815")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 815,
    width = 1201,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    600.0,
    407.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    890.5,
    332.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
)
entry_1.place(
    x=628.0,
    y=28.0,
    width=525.0,
    height=607.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_screenshot("test.png"),
    relief="flat"
)
button_1.place(
    x=481.0,
    y=717.0,
    width=205.0,
    height=66.01260375976562
)

canvas.create_rectangle(
    -1.0,
    660.0,
    1215.0,
    661.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    588.75,
    -0.9991455078125,
    589.75,
    661.0029296875,
    fill="#000000",
    outline="")


image_image_2 = PhotoImage(file="test.png")
image_2 = canvas.create_image(
    290.0,
    332.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
