import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=640, height=480, bg='white')

canvas.pack()

def draw(event):
    x, y = event.x, event.y
    r = 5
    canvas.create_oval(x - r, y - r, x + r, y + r, fill='black')

canvas.bind('<B1-Motion>', draw)
root.mainloop()