from tkinter import * 
a=3
b=0
c=0
d=0
def Face():
	global a,draw
	if a==0:
		draw.create_oval((5, 5, 290, 290))
		a=1
	elif a==1:
		draw.create_rectangle((15, 15, 290, 290), width="2")
	else:
		pass
		
def Nose():
	draw.create_polygon([(150, 200), (150, 15), (15,150 )],fill="black")
tk=Tk()
tk.title("Фоторобот")
tk.geometry("700x300")
f1=Frame(tk,width=300,height=300)
f2=Frame(tk,width=400,height=300)
draw=Canvas(f2,width=300,height=300,bg="green")
draw.pack()
f1.pack(side=LEFT)
f2.pack(side=RIGHT)
name=Label(f1,text="Создание фоторобота",font="Calibri 26",fg="black",bg="lightblue",justify=CENTER)
name.pack(side=TOP)
face=Checkbutton(f1,text="Лицо",font="Calibri 26",fg="black",bg="lightgreen",relief=GROOVE,command=Face)
mouth=Checkbutton(f1,text="Рот",font="Calibri 26",fg="black",bg="lightgreen",relief=GROOVE)
nose=Checkbutton(f1,text="Нос",font="Calibri 26",fg="black",bg="lightgreen",relief=GROOVE,command=Nose)
eyes=Checkbutton(f1,text="Глаза",font="Calibri 26",fg="black",bg="lightgreen",relief=GROOVE)

face.pack()
mouth.pack()
nose.pack()
eyes.pack()

tk.mainloop()