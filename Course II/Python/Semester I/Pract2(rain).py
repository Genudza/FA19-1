"""
На экране постоянно генерируются контрастные “капли”, равномерно движущиеся вниз.
1)Поэкспериментируйте с плотностью генерации капель.
2)Капли должны создавать ощущение трехмерности - дальние движутся медленнее и меньше в размерах.
"""
import tkinter as tk
from random import randint

class Raindrop:
    def __init__(self, canvas, width, height, x, y, yspeed, length, width_line,  color="#00bfff"):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.yspeed = yspeed
        self.length = length
        self.line = canvas.create_line(self.x, self.y+self.length, self.x, self.y, fill=color, width=width_line)
        

    def moving(self):
        self.y += self.yspeed
        self.canvas.move(self.line, 0, self.yspeed)

        # Если выходит за границы canvas
        if self.y > self.height:
            self.canvas.move(self.line, 0, -(self.height+self.length))
            self.y -= self.height + self.length

def redraw():
    for drop in drops:
        drop.moving()

    root.after(10, redraw)


root = tk.Tk()
root.title("Дождь")
width = 600
height = 600
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()
drops = []
# Основной список цветов
colors = [*["blue"]*3, *["blue2"]*3, *["#77a1b5"]*3, *["#6996D3"]*3]
# colors = [*["#6557E9"]*3, *["#0000cc"]*3, *["#000099"]*3, *["#6996D3"]*3]
# Градиент
# colors = ["blue2","blue", "dodger blue", "RoyalBlue2", "RoyalBlue1", "cornflower blue", "DeepSkyBlue2", "SteelBlue2", "SteelBlue1", "SkyBlue2","SkyBlue1"]
print(list(reversed(colors)))
print(list(reversed(colors))[int(11)])
# default: step = 1.5; min_len = 4; max_len = 15;
step = 1.5 # коэффициент изменение длины полосок
min_len = 4
max_len = 15
col_range = max_len - len(colors) + 1 # нужен для реализации шага
# print(col_range)
for i in range(100):
    length = randint(min_len, max_len)*step
    width_line = 0.09 * length
    # print(length, list(reversed(colors))[int(length//step)-col_range])
    if length > 14:
        drops.append(Raindrop(canvas, width, height, x=randint(0, width), y=randint(0, height), yspeed=randint(5, 9), length=length, color=list(reversed(colors))[int(length//step)-col_range], width_line=width_line))

    if length <15:
        drops.append(Raindrop(canvas, width, height, x=randint(0, width), y=randint(0, height), yspeed=randint(2, 4), length=length,color=list(reversed(colors))[int(length//step)-col_range], width_line=width_line))


redraw()

root.mainloop()