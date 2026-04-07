import tkinter as tki
import time
width = 800
height = 200
canvas = tki.Canvas(width=width, height=height)
canvas.pack()

rect = canvas.create_rectangle(10, 10, 100, 100, fill="blue")
i = 10
count = 0
x = False
while True:
    
    canvas.move(rect, i, 0)
    count += 1
    if count == width / i and x == False:
        count = 0
        i *= -1
        x = True
    elif count == width / i and x == True:
        count = 0
        i *= -1
        x = False
    canvas.update()
    time.sleep(0.2)

tki.mainloop()