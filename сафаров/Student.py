from human import Human
from tkinter import *

class Student(Human):
	def __init__(self, canvas, name, x, y, g, v, gen, hp):
		super().__init__(canvas, name, x, y, gen, hp)
		self.__group = g
		self.__var = v

	def _TEXT(self) : 
		self.canvas.create_text(self.x+60, self.y-290, text=f'{self.name}', justify=CENTER, font="Verdana 13")

