import tkinter as tki
import time
width = 800
height = 500
canvas = tki.Canvas(width=width, height=height)
canvas.pack()
rect = canvas.create_rectangle(10, 10, 300, 100, fill="red")
rect = canvas.create_rectangle(10, 100, 300, 200, fill="white")
rect = canvas.create_rectangle(10, 200, 300, 300, fill="blue")
tki.mainloop()