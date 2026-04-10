import tkinter as tki
import time
width = 800
height = 500
canvas = tki.Canvas(width=width, height=height)
canvas.pack()
rect = canvas.create_rectangle(10, 10, 50, 100, fill="green")
rect = canvas.create_rectangle(50, 10, 90, 100, fill="white")
rect = canvas.create_rectangle(90, 10, 140, 100, fill="orange")
tki.mainloop()