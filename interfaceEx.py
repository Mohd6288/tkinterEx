import tkinter as tk
from turtle import TurtleScreen, RawTurtle
import colorsys
import random

# -------------------------------
# Tkinter window
# -------------------------------
root = tk.Tk()
root.title("Centered Generative Art")
root.geometry("900x600")
root.config(bg="#1a1a1a")

# -------------------------------
# Canvas for Turtle
# -------------------------------
canvas = tk.Canvas(root, width=600, height=600, bg="black")
canvas.place(x=20, y=0)

screen = TurtleScreen(canvas)
screen.bgcolor("black")
t = RawTurtle(screen)
t.speed(0)
t.hideturtle()

# -------------------------------
# Draw shapes centered
# -------------------------------
def draw_shape():
    t.clear()
    t.pensize(int(size_entry.get()))
    num = int(num_entry.get())
    step = int(step_entry.get())
    shape = shape_var.get()
    color_mode = color_var.get()

    for i in range(num):
        # Always start from center
        t.penup()
        t.goto(0, 0)
        t.pendown()

        # Color mode
        if color_mode == "Dark":
            gray = random.uniform(0.2, 0.9)
            t.pencolor(gray, gray, gray)
        else:
            t.pencolor(colorsys.hsv_to_rgb(i / num, 1, 1))

        # Rotate a bit for generative effect
        t.setheading(i * (360 / num))

        # Draw selected shape
        if shape == "Circle":
            t.circle(step)
        elif shape == "Triangle":
            for _ in range(3):
                t.forward(step)
                t.left(120)
        elif shape == "Square":
            for _ in range(4):
                t.forward(step)
                t.right(90)

        # Slight forward for layering effect
        t.penup()
        t.forward(step / 3)
        t.pendown()

# -------------------------------
# UI Controls
# -------------------------------

tk.Label(root, text="🎨 Centered Generative Art",
         font=("Arial", 18, "bold"), fg="white", bg="#1a1a1a").place(x=640, y=20)

# Number of shapes
tk.Label(root, text="Number of shapes:", fg="white", bg="#1a1a1a").place(x=640, y=80)
num_entry = tk.Entry(root, width=12)
num_entry.place(x=640, y=105)
num_entry.insert(0, "60")

# Shape size / step
tk.Label(root, text="Size/Step:", fg="white", bg="#1a1a1a").place(x=640, y=150)
step_entry = tk.Entry(root, width=12)
step_entry.place(x=640, y=175)
step_entry.insert(0, "60")

# Line thickness
tk.Label(root, text="Line thickness:", fg="white", bg="#1a1a1a").place(x=640, y=220)
size_entry = tk.Entry(root, width=12)
size_entry.place(x=640, y=245)
size_entry.insert(0, "2")

# Shape selection
tk.Label(root, text="Shape:", fg="white", bg="#1a1a1a").place(x=640, y=280)
shape_var = tk.StringVar()
shape_var.set("Circle")
shape_menu = tk.OptionMenu(root, shape_var, "Circle", "Triangle", "Square")
shape_menu.config(width=10)
shape_menu.place(x=640, y=305)

# Color mode
tk.Label(root, text="Color mode:", fg="white", bg="#1a1a1a").place(x=640, y=350)
color_var = tk.StringVar()
color_var.set("Dark")
color_menu = tk.OptionMenu(root, color_var, "Dark", "Rainbow")
color_menu.config(width=10)
color_menu.place(x=640, y=375)

# Buttons
tk.Button(root, text="Generate Art 🎨", font=("Arial", 14, "bold"),
          bg="#4CAF50", fg="white", command=draw_shape).place(x=640, y=420)
tk.Button(root, text="Clear ❌", font=("Arial", 12),
          bg="#EF5350", fg="white", command=lambda: t.clear()).place(x=640, y=470)

root.mainloop()
