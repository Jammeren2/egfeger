from tkinter import Tk, Canvas, ARC, SE, W
from grid import Grid
from human import Human
from Student import Student

from random import sample, randint

with open('12.txt', 'r', encoding='utf-8') as file:
    stst = file.readlines()


root = Tk()
canvas = Canvas (root,width=800,height=600)
canvas.pack()

grid = Grid(canvas)
grid.display()


st = sample(stst, 4)

x = [50, 220, 420, 620]
y = [350, 500, 350, 500]


for i, stst in enumerate(st):
	data = stst.strip().split(';')

	fname = data[1] #полное имя
	var = int(data[3]) #вариант
	gen = data[2]

	hp = randint(0, 100)

	lname, *ins = fname.split() #фамилия
	ins = ' '.join([name[0] + '.' for name in ins]) #инициалы

	student = Student(canvas, x[i], y[i], f'{lname} {ins}', 'ИП-21', var, gen, hp)
	student.display()
	print(f'{lname} {ins}, HP: {hp}')

root.mainloop()
