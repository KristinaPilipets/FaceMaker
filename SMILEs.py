from tkinter import * 

def Face():
	draw.create_oval((5, 5, 290, 290),fill="pink",outline="black")

def Nose():
	draw.create_polygon([(150, 163), (181, 163), (150,130 )],fill="grey")

def Mouth():
	draw.create_line((213, 215, 90, 215),fill="black",width=3)

def Eyes():
	draw.create_oval((72,72,130,130),fill="white")
	draw.create_oval((165,72,221,130),fill="white")
	draw.create_oval((82,82,117,120),fill="black")
	draw.create_oval((175,82,211,120),fill="black")

def Freckles():
	draw.create_line((198,145,200,145),fill="brown",width=2)
	draw.create_line((227,169,230,169),fill="brown",width=2)
	draw.create_line((130,127,133,127),fill="brown",width=2)
	draw.create_line((147,173,150,173),fill="brown",width=2)
	draw.create_line((146,150,150,150),fill="brown",width=2)
	draw.create_line((80,134,82,134),fill="brown",width=2)
	draw.create_line((174,181,177,181),fill="brown",width=2)
	draw.create_line((155,91,158,91),fill="brown",width=2)
	draw.create_line((119,150,122,150),fill="brown",width=2)
	draw.create_line((108,145,111,145),fill="brown",width=2)
	draw.create_line((241,129,244,129),fill="brown",width=2)
	draw.create_line((111,193,113,193),fill="brown",width=2)

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
mouth=Checkbutton(f1,text="Рот",font="Calibri 26",fg="black",bg="lightgreen",relief=GROOVE,command=Mouth)
nose=Checkbutton(f1,text="Нос",font="Calibri 26",fg="black",bg="lightgreen",relief=GROOVE,command=Nose)
eyes=Checkbutton(f1,text="Глаза",font="Calibri 26",fg="black",bg="lightgreen",relief=GROOVE,command=Eyes)
freckles=Checkbutton(f1,text="веснушки",font="Calibri 26",fg="black",bg="lightgreen",relief=GROOVE,command=Freckles)
face.pack()
mouth.pack()
nose.pack()
eyes.pack()
freckles.pack()

tk.mainloop()