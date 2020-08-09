from tkinter import*
import sqlite3 as sql
from subwindow import render


connect  = sql.connect('mydatabase.db')
cursor = connect.cursor()

# cursor.execute("""
# 	CREATE TABLE students(
# 	      first_name  text,
# 	      last_name  text,
# 	      phone_number text
# 	)

# 	""")
# cursor.execute("INSERT INTO students values('Ashraf' , 'Hossain', '01928419790') ")
# cursor.execute("INSERT INTO students values ('Israfil' , 'Hossain' , '01927246714')")ha

def doit(a ,b ,c , d):
	render(a , b , c, d)



def render2():
	x = input1.get()
	with connect:
		cursor.execute("SELECT *FROM students WHERE first_name = ?" , (x,))
	xx = cursor.fetchall()
	print(xx)
	name = xx[0][0] + '.gif'
	with open(name , 'wb') as w:
		w.write(xx[0][3])
	Label(window , text = xx[0][0] + "  " + xx[0][2]).grid(row =  5 , column = 2)
	print(name)
	Button(window , text = "FORM" ,  width = 10 ,command = lambda : doit(xx[0][0] , xx[0][1] , xx[0][2], name)).grid(row = 1 + 5)




# connect.close()


# def render2():
# 	x = input1.get()
# 	cursor.execute("SELECT *FROM students WHERE first_name = ? " , (x,))
# 	connect.commit()
# 	connect.close()
# 	# lab["text"] = cursor.fetchall()
# 	print(cursor.fetchall())

window = Tk()
window.title("SQL INTERFACE")
Label(window, text = "Here goes your Data Entries").grid(row = 0)
Label(window , text = "Enter your First Name").grid(row = 1)
Label(window , text = "Enter your Last Name ").grid(row = 2)
input1 = Entry(window)
input2  = Entry(window)

input1.grid(row = 1 , column = 1)
input2.grid(row = 2 , column = 1)

Button(window , text = "click" , width = 10 , command = render2).grid(row = 3)
window.mainloop()

