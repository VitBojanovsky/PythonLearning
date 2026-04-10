import tkinter as tki
import time
width = 800
height = 500
canvas = tki.Canvas(width=width, height=height)
canvas.pack()
i = 20
z = 0
colors = ["red", "blue", "green", "yellow"]
for i in range(20, 50, 10): 
    rect = canvas.create_rectangle(10+i, 10+i, 100-i, 100-i, fill=colors[z % len(colors)])
    z+=1

tki.mainloop()