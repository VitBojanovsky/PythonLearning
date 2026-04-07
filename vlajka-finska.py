import tkinter as tki
import time
width = 800
height = 500
canvas = tki.Canvas(width=width, height=height)
canvas.pack()
rect = canvas.create_rectangle(10, 10, 50, 100, fill="white")
rect = canvas.create_rectangle(50, 10, 90, 100, fill="blue")
rect = canvas.create_rectangle(90, 10, 200, 100, fill="white")

rect = canvas.create_rectangle(10, 100, 200, 50, fill="blue")

rect = canvas.create_rectangle(10, 140, 50, 100, fill="white")
rect = canvas.create_rectangle(50, 140, 90, 100, fill="blue")
rect = canvas.create_rectangle(90, 140, 200, 100, fill="white")



tki.mainloop()