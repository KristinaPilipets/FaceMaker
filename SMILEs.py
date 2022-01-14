from tkinter import * 
faec=""
def Face():
	global faec
	if var_face.get()=="лицо":
		faec=draw.create_oval((5, 5, 290, 290),fill="pink",outline="black")
	else:
		draw.delete(faec)

eye=""
def Nose():
	global eye
	if var_nose.get()=="нос":
		eye=draw.create_polygon([(150, 163), (181, 163), (150,130 )],fill="grey")
	else:
		draw.delete(eye)

a=""
def Mouth():
	global a
	if var_mouth.get()=="рот":
		a=draw.create_line((213, 215, 90, 215),fill="black",width=3)
	else:
		draw.delete(a)

b=c=d=e=""
def Eyes():
	global b,c,d,e
	if var_eyes.get()=="глаза":
		b=draw.create_oval((72,72,130,130),fill="white")
		c=draw.create_oval((165,72,221,130),fill="white")
		d=draw.create_oval((82,82,117,120),fill="black")
		e=draw.create_oval((175,82,211,120),fill="black")
	else:
		draw.delete(b,c,d,e)

a1=a2=a3=a4=a5=a6=a7=a8=a9=a10=a11=a12=""
def Freckles():
	global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12
	if var_freckles.get()=="весн":
		a1=draw.create_line((198,145,200,145),fill="brown",width=2)
		a2=draw.create_line((227,169,230,169),fill="brown",width=2)
		a3=draw.create_line((130,127,133,127),fill="brown",width=2)
		a4=draw.create_line((147,173,150,173),fill="brown",width=2)
		a5=draw.create_line((146,150,149,150),fill="brown",width=2)
		a6=draw.create_line((80,134,82,134),fill="brown",width=2)
		a7=draw.create_line((174,181,177,181),fill="brown",width=2)
		a8=draw.create_line((155,91,158,91),fill="brown",width=2)
		a9=draw.create_line((119,150,122,150),fill="brown",width=2)
		a10=draw.create_line((108,145,111,145),fill="brown",width=2)
		a11=draw.create_line((241,129,244,129),fill="brown",width=2)
		a12=draw.create_line((111,193,113,193),fill="brown",width=2)
	else:
		draw.delete(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)

tk=Tk()
tk.title("Фоторобот")
tk.geometry("700x350")
f1=Frame(tk,width=300,height=350)
f2=Frame(tk,width=400,height=350)
draw=Canvas(f2,width=300,height=300,bg="lightgreen")
draw.pack()
f1.pack(side=LEFT)
f2.pack(side=RIGHT)
name=Label(f1,text="Создание фоторобота",font="Calibri 26",fg="black",bg="lightblue",justify=CENTER)
name.pack(side=TOP)

var_face=StringVar()
face=Checkbutton(f1,text="Лицо",font="Calibri 26",fg="black",bg="green",relief=GROOVE,variable=var_face,offvalue="убрать",onvalue="лицо",command=Face)
face.deselect()

var_mouth=StringVar()
mouth=Checkbutton(f1,text="Рот",font="Calibri 26",fg="black",bg="green",relief=GROOVE,variable=var_mouth,onvalue="рот",offvalue="убрать",command=Mouth)
mouth.deselect()

var_nose=StringVar()
nose=Checkbutton(f1,text="Нос",font="Calibri 26",fg="black",bg="green",relief=GROOVE,variable=var_nose,onvalue="нос",offvalue="убрать",command=Nose)
nose.deselect()

var_eyes=StringVar()
eyes=Checkbutton(f1,text="Глаза",font="Calibri 26",fg="black",bg="green",relief=GROOVE,variable=var_eyes,onvalue="глаза",offvalue="убрать",command=Eyes)
eyes.deselect()

var_freckles=StringVar()
freckles=Checkbutton(f1,text="веснушки",font="Calibri 26",fg="black",bg="green",relief=GROOVE,variable=var_freckles,onvalue="весн",offvalue="убрать",command=Freckles)
freckles.deselect()

face.pack()
mouth.pack()
nose.pack()
eyes.pack()
freckles.pack()

tk.mainloop()