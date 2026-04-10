import tkinter as tki
import time
width = 800
height = 500
canvas = tki.Canvas(width=width, height=height)
canvas.pack()

rect = canvas.create_rectangle(10, 10, 100, 20, fill="red")
rect = canvas.create_rectangle(90, 10, 100, 80, fill="blue")
rect = canvas.create_rectangle(10, 80, 100, 90, fill="red")
rect = canvas.create_rectangle(10, 20, 20, 90, fill="blue")

tki.mainloop()