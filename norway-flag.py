import tkinter as tki
import time
width = 800
height = 500
canvas = tki.Canvas(width=width, height=height)
canvas.pack()
rect = canvas.create_rectangle(10, 10, 200, 100, fill="red")
rect = canvas.create_rectangle(10, 40, 200, 70, fill="white")
rect = canvas.create_rectangle(40, 10, 70, 100, fill="white")
rect = canvas.create_rectangle(10, 50, 200, 60, fill="blue")
rect = canvas.create_rectangle(50, 10, 60, 100, fill="blue")




tki.mainloop()