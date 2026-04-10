import tkinter as tki
import time
width = 800
height = 500
canvas = tki.Canvas(width=width, height=height)
canvas.pack()

rect = canvas.create_rectangle(10, 10, 50, 50, fill="red")
rect = canvas.create_rectangle(20, 20, 60, 60, fill="blue")
rect = canvas.create_rectangle(30, 30, 70, 70, fill="green")
rect = canvas.create_rectangle(40, 40, 80, 80, fill="yellow")

tki.mainloop()