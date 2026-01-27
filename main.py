from pyray import *
init_window(800, 450, "Hello")
circle_x = 200
circle_y = 200
velocity_x = 2
velocity_y = 2
while not window_should_close():
    circle_x += velocity_x
    circle_y += velocity_y
    
    if circle_x > 800 - 50 or circle_x < 50:
        velocity_x *= -1
    if circle_y > 450 - 50 or circle_y < 50:
        velocity_y *= -1
    
    begin_drawing()
    clear_background(WHITE)
    draw_text("Hello world", 190, 200, 20, BLUE)
    for i in range(50):
        draw_circle(int(circle_x), int(circle_y), i , RED)
    set_target_fps(60)
    end_drawing()
close_window()