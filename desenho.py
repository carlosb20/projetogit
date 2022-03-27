from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor


class Pinturas:
    def __init__(self,master) -> None:
        self.root = master

        self.canvas = Canvas(self.root,width=33,height=300,bg ='white',bd=2,relief='solid')
        self.canvas.place(x=0,y=0)

        self.linha = Canvas(self.root,width=730,height=300,bg ='white',cursor='hand2',bd=1,relief='solid')
        self.linha.bind('<B1-Motion>',self.create_linha)
        self.linha.bind("<Button>",self.addlinha)
        self.linha.place(x=40,y=0)

        self.x = 0
        self.y = 0

        self.cor = 'black'

        self.quadrado()

       
        self.scala = ttk.Scale(self.root,from_= 0,to = 100,length=200,command=self.escala)
        self.scala.place(x=0,y=350)

        self.label = Label(self.root,text = '% 0')
        self.label.place(x=90,y=340)

        self.delete = Button(self.canvas,text='deleta',command=self.delete_linha)
        self.delete.place(x=0,y=150)


    def quadrado(self):

        id = self.canvas.create_rectangle(10,10,30,30,fill='red')
        self.canvas.tag_bind(id,'<Button-1>',lambda x : self.show_color('red'))

        id = self.canvas.create_rectangle(10,40,30,60,fill='blue')
        self.canvas.tag_bind(id,'<Button-1>',lambda x : self.show_color('blue'))

        id = self.canvas.create_rectangle(10,70,30,90,fill='green')
        self.canvas.tag_bind(id,'<Button-1>',lambda x : self.show_color('green'))

        id = self.canvas.create_rectangle(10,100,30,120,fill='orange')
        self.canvas.tag_bind(id,'<Button-1>',lambda x : self.show_color('orange'))



    def show_color(self,color):
        self.cor = color

    def delete_linha(self):
        self.linha.delete('all')


    def addlinha(self,val):
        self.x = val.x
        self.y = val.y   

    def create_linha(self,s):
       
        self.linha.create_line(self.x,self.y,s.x,s.y,fill=self.cor,width=int(self.scala.get()),capstyle="round")
        self.x,self.y = s.x,s.y

    def escala(self,x):
        self.label['text'] = f'% {self.scala.get():.0f}'
        

root = Tk()
res = Pinturas(root)
root.geometry('900x500')
root.mainloop()

