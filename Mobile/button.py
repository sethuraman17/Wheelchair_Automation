import tkinter as tk

def on_mouse_drag(event):
    x, y = event.x, event.y
    # print(f'Joystick X: {x}, Y: {y}')
    if x > 95:
        print('Right')
    elif y < -30:
        print('Forward')
    elif x < -75:
        print('Left')
    elif y > 90:
        print('Backward')

def on_mouse_release(event):
    print('Joystick Released')

def forward():
    print('Forward')

def backward():
    print('Backward')

def right():
    print('Right')

def left():
    print('Left')


root = tk.Tk()
root.geometry('640x480')
root.title('Mobile Control')

forward_button = tk.Button(root, text='Forward', command=forward)
backward_button = tk.Button(root, text='Backward', command=backward)
right_button = tk.Button(root, text='Right', command=right)
left_button = tk.Button(root, text='Left', command=left)

forward_button.place(x=290, y=80)
backward_button.place(x=290, y=250)
right_button.place(x=170, y=150)
left_button.place(x=430, y=150)

# Create the joystick (a simple rectangle) and place it in the center
joystick = tk.Canvas(root, width=50, height=50, bg='blue')
joystick.place(x=295, y=155)

# Bind mouse events to the joystick
joystick.bind('<B1-Motion>', on_mouse_drag)
joystick.bind('<ButtonRelease-1>', on_mouse_release)

root.mainloop()
