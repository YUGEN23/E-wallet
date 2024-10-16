
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"J:\Python programming file\test gui e-wallet\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("430x932")
window.configure(bg = "#F0EDED")


canvas = Canvas(
    window,
    bg = "#F0EDED",
    height = 932,
    width = 430,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    430.0,
    103.93881225585938,
    fill="#AF52DE",
    outline="")

canvas.create_text(
    174.5,
    56.851806640625,
    anchor="nw",
    text="Pay Bills",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_rectangle(
    121.9931640625,
    153.0,
    136.9931640625,
    168.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    29.0,
    51.96942138671875,
    54.0,
    76.96942138671875,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    29.0,
    134.34664916992188,
    400.0,
    190.99636840820312,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    40.2054443359375,
    137.6715087890625,
    90.2054443359375,
    187.6715087890625,
    fill="#000000",
    outline="")

canvas.create_text(
    100.0,
    151.6715087890625,
    anchor="nw",
    text="Search Billers",
    fill="#C1AFAF",
    font=("Inter SemiBold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
