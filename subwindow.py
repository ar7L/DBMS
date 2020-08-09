from tkinter import*
import tkinter


# window = Tk()
# window.geometry("600x500")
# window.title("Hello world")
# photo = ''

img = ""

def take(a , b, c):
	 L1  = Label(window , text = a)
	 L2 = Label(window , text = b)
	 L3 = Label(window , text = c)
	 L1.place(x = 150 , y = 10)
	 L2.place(x = 150 , y = 50)
	 L3.place(x = 150 , y = 90)

# def addImage():
# 	global img 
# 	img = PhotoImage(file  = photo)
# 	L4 = Label(window ,image = img )
# 	L4.pack()
# 	L4.place(x = 350 , y = 10)


def render(fn , ln , ph , pic):
	# window = Tk()
	# window.geometry("600x500")
	# window.title("Hello world")
	window = Toplevel()
	window.geometry("600x500")
	window.title("INFORMATION")
	global photo
	photo = pic
	La = Label(window , text = "First Name : ")
	Lb = Label(window , text = "Last Name : ")
	Lc = Label(window , text = "Phone Number : ")
	La.place(x = 10 , y =10)
	Lb.place(x = 10,  y = 50)
	Lc.place(x = 10 , y = 90)
	L1  = Label(window , text = fn)
	L2 = Label(window , text = ln)
	L3 = Label(window , text = ph)
	L1.place(x = 150 , y = 10)
	L2.place(x = 150 , y = 50)
	L3.place(x = 150 , y = 90)
	# take(fn , ln , ph)
	global img
	img = PhotoImage(file  = photo)
	L4 = Label(master  = window , image = img)
	L4.image = img
	L4.pack()
	L4.place(x = 350 , y = 10)
	print(photo)
	window.mainloop()

print(img)