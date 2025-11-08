import tkinter as tk
from turtle import TurtleScreen, RawTurtle
from tkinter import ttk

# ------------------------------------
# إنشاء نافذة Tkinter
# ------------------------------------
root = tk.Tk()
root.title("🎨 برنامج الرسم الإبداعي - Tkinter + Turtle")
root.geometry("700x500")
root.config(bg="#e8eef1")

# ------------------------------------
# مكان الرسم (Canvas + Turtle)
# ------------------------------------
canvas_frame = tk.Frame(root)
canvas_frame.place(x=20, y=20)

canvas = tk.Canvas(canvas_frame, width=450, height=450)
canvas.pack()

screen = TurtleScreen(canvas)
screen.bgcolor("white")
t = RawTurtle(screen)
t.speed(0)

# ------------------------------------
# دوال الرسم
# ------------------------------------
def draw_square():
    t.clear()
    t.color(color_var.get())
    side = size_var.get()
    for _ in range(4):
        t.forward(side)
        t.right(90)

def draw_star():
    t.clear()
    t.color(color_var.get())
    size = size_var.get()
    for _ in range(5):
        t.forward(size)
        t.right(144)

def draw_circle():
    t.clear()
    t.color(color_var.get())
    t.circle(size_var.get())

def draw_heart():
    t.clear()
    t.color(color_var.get())
    size = size_var.get()
    t.begin_fill()
    t.left(45)
    t.forward(size)
    t.circle(size/2, 180)
    t.right(90)
    t.circle(size/2, 180)
    t.forward(size)
    t.end_fill()

def clear_screen():
    t.clear()

# ------------------------------------
# عناصر التحكم على اليمين
# ------------------------------------

# اختيار اللون
tk.Label(root, text="اختر اللون:", font=("Arial", 12), bg="#e8eef1").place(x=500, y=40)
color_var = tk.StringVar()
colors = ["red", "blue", "green", "purple", "orange", "black"]
color_menu = ttk.Combobox(root, textvariable=color_var, values=colors, width=10)
color_menu.place(x=500, y=70)
color_menu.set("black")

# حجم الشكل
tk.Label(root, text="حجم الرسم:", font=("Arial", 12), bg="#e8eef1").place(x=500, y=120)
size_var = tk.IntVar()
size_slider = tk.Scale(root, from_=50, to=200, orient="horizontal", variable=size_var, bg="#e8eef1")
size_slider.place(x=500, y=150)
size_slider.set(100)

# أزرار لرسم الأشكال
ttk.Button(root, text="مربع 🟦", width=12, command=draw_square).place(x=500, y=230)
ttk.Button(root, text="نجمة ⭐", width=12, command=draw_star).place(x=500, y=270)
ttk.Button(root, text="دائرة ⚫", width=12, command=draw_circle).place(x=500, y=310)
ttk.Button(root, text="قلب ❤️", width=12, command=draw_heart).place(x=500, y=350)

# زر مسح الشاشة
ttk.Button(root, text="مسح الرسم ✖", width=12, command=clear_screen).place(x=500, y=400)

root.mainloop()
