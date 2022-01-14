from tkinter import * 

def faceparts():
	draw.delete("all")
	if var_1.get()=="лицо":
		draw.create_oval((5, 5, 290, 290),fill="pink",outline="black")
	else:
		pass
	if var_2.get()=="глаза":
		draw.create_oval((72,72,130,130),fill="white")
		draw.create_oval((165,72,221,130),fill="white")
		draw.create_oval((82,82,117,120),fill="black")
		draw.create_oval((175,82,211,120),fill="black")
	else:
		pass
	if var_3.get()=="нос":
		draw.create_polygon([(150, 163), (181, 163), (150,130 )],fill="grey")
	else:
		pass
	if var_4.get()=="рот":
		draw.create_line((213, 215, 90, 215),fill="black",width=3)
	else:
		pass
	if var_5.get()=="весн":
		draw.create_line((198,145,200,145),fill="brown",width=2)
		draw.create_line((227,169,230,169),fill="brown",width=2)
		draw.create_line((130,127,133,127),fill="brown",width=2)
		draw.create_line((147,173,150,173),fill="brown",width=2)
		draw.create_line((146,150,149,150),fill="brown",width=2)
		draw.create_line((80,134,82,134),fill="brown",width=2)
		draw.create_line((174,181,177,181),fill="brown",width=2)
		draw.create_line((155,91,158,91),fill="brown",width=2)
		draw.create_line((119,150,122,150),fill="brown",width=2)
		draw.create_line((108,145,111,145),fill="brown",width=2)
		draw.create_line((241,129,244,129),fill="brown",width=2)
		draw.create_line((111,193,113,193),fill="brown",width=2)
	else:
		pass
tk=Tk()
tk.title("Фоторобот")
tk.geometry("700x400")
f1=Frame(tk,width=300,height=400)
f2=Frame(tk,width=400,height=400)
draw=Canvas(f2,width=300,height=300,bg="lightgreen")
draw.pack()
f1.pack(side=LEFT)
f2.pack(side=RIGHT)
name=Label(f1,text="Создание фоторобота",font="Calibri 26",fg="black",bg="lightblue",justify=CENTER)
name.pack(side=TOP)

var_1=StringVar()
face=Checkbutton(f1,text="Лицо",font="Calibri 26",fg="black",bg="green",relief=GROOVE,variable=var_1,offvalue="убрать",onvalue="лицо")
face.deselect()

var_4=StringVar()
mouth=Checkbutton(f1,text="Рот",font="Calibri 26",fg="black",bg="green",relief=GROOVE,variable=var_4,onvalue="рот",offvalue="убрать")
mouth.deselect()

var_3=StringVar()
nose=Checkbutton(f1,text="Нос",font="Calibri 26",fg="black",bg="green",relief=GROOVE,variable=var_3,onvalue="нос",offvalue="убрать")
nose.deselect()

var_2=StringVar()
eyes=Checkbutton(f1,text="Глаза",font="Calibri 26",fg="black",bg="green",relief=GROOVE,variable=var_2,onvalue="глаза",offvalue="убрать")
eyes.deselect()

var_5=StringVar()
freckles=Checkbutton(f1,text="веснушки",font="Calibri 26",fg="black",bg="green",relief=GROOVE,variable=var_5,onvalue="весн",offvalue="убрать")
freckles.deselect()

creat=Button(f1,text="создать",font="Calibri 26",fg="black",bg="green",relief=GROOVE,command=faceparts)

creat.pack(side=TOP)
face.pack()
mouth.pack()
nose.pack()
eyes.pack()
freckles.pack()

tk.mainloop()
