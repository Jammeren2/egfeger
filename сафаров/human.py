from tkinter import *

class Human() :
    def __init__ (self, canvas, x, y, name, gen, hp):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.name = name
        self.gen = gen
        self.hp = hp

    def display(self):

        self._drawHead()
        self._drawBody()
        self._hp()
        self._TEXT()

        
    def _drawHead(self) :
        self.canvas.create_oval(self.x, self.y-170, self.x+100, self.y-270, width=2)

        
        self.canvas.create_arc(self.x+24, self.y-200, self.x+69, self.y-230, start=0, extent=-180, style=ARC, outline="blue", width=3)
        
        self.canvas.create_oval(self.x+60, self.y-220, self.x+75, self.y-235, width=0, fill="red")# ПРАВый глаз
        
        self.canvas.create_oval(self.x+15, self.y-220, self.x+30, self.y-235, width=0, fill="red")# ЛЕВый глаз






        if self.gen=='м':
            self.canvas.create_line(self.x+35,self.y-265, self.x+30,self.y-275)
            self.canvas.create_line(self.x+50,self.y-265, self.x+50,self.y-280)
            self.canvas.create_line(self.x+65,self.y-265, self.x+70,self.y-275)
        else:
            self.canvas.create_line(self.x+25,self.y-175, self.x+10,self.y-150)
            self.canvas.create_line(self.x+75,self.y-175, self.x+90,self.y-150)
        


    def _hp(self):

        hpt = (self.hp * 140 / 100)

        # Рисуем полосу прочности
        self.canvas.create_rectangle(self.x - 20, self.y - 350,
                                     self.x - 20 + hpt, self.y - 315,
                                     fill='green')

        self.canvas.create_line(self.x - 20, self.y - 350,
                                self.x - 20, self.y - 315,
                                self.x + 120, self.y - 315,
                                self.x + 120, self.y - 350,
                                self.x - 20, self.y - 350,
                                fill='black', width=2)








    def _drawBody(self) :
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+50, self.y-170, width=2)# тело
 
        self.canvas.create_line(self.x, self.y-110, self.x+50, self.y-150, self.x+100, self.y-110, width=2)# руки

        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+100, self.y, width=2)# ноги
        

          
    def _TEXT(self) : 
        self.canvas.create_text(self.x+50, self.y-300, 
              text=self.name, justify=CENTER, font="Times")

              
        
        
        
        
        
