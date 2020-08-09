import sqlite3 as sql
from subwindow import render

class DATA:
	def __init__(self , first , last , phone ,img = None):
		self.first = first
		self.last = last
		self.phone = phone
		self.img = img
class data:
	def __init__(self , first , last , phone ):
		self.first = first
		self.last = last
		self.phone = phone
		# self.img = img


connect  = sql.connect('mydatabase.db')

cursor = connect.cursor()



# cursor.execute("""
# 	CREATE TABLE students(
# 	      first_name  text,
# 	      last_name  text,
# 	      phone_number text,
# 	      dp BLOP
# 	)

# 	""")

# info = DATA("Ashraf" , "Hossain" , "01928419790")

# cursor.execute("INSERT INTO students values('Ashraf' , 'Hossain', '01928419790') ")
# cursor.execute("INSERT INTO students values(? , ? , ?)" , (info.first , info.last , info.phone))
# cursor.execute("DELETE FROM students WHERE first_name = ? AND last_name = ? AND phone_number= ?" , ('Ashraf' , 'Hossain' , '01928419790'))





def PUSH(info):
	cursor.execute("SELECT *FROM students WHERE first_name = ? AND last_name = ? AND phone_number = ? ", (info.first , info.last, info.phone))
	f = cursor.fetchone()
	if f != None:
		print("Already exists")
		return
	with connect:
		cursor.execute("INSERT INTO students values(:first , :last, :phone , :dp)" , {'first' : info.first , 'last' : info.last , 'phone': info.phone, 'dp' : img})
def OUT(info):
	cursor.execute("SELECT *FROM students WHERE first_name = ? AND last_name = ? AND phone_number = ? ", (info.first , info.last, info.phone))
	return (cursor.fetchall())
def WILD(X):
# cursor.execute("DELETE FROM students WHERE first_name = ? AND last_name = ? AND phone_number= ?" , ('Ashraf' , 'Hossain' , '01928419790'))
	cursor.execute("SELECT *FROM students WHERE phone_number LIKE  ?" , X+'%')
	print(cursor.fetchall())
def DEL(info):
    cursor.execute("DELETE FROM students WHERE first_name = ? AND last_name = ? AND phone_number= ?" , (info.first , info.last , info.phone))



with open('ashraf.gif' , 'rb') as f:
	img = f.read()
# with open('ashraf.gif' , 'wb') as w:
# 	w.write(img)

# info = DATA('ashraf' , 'hossain' , '01928419790' , img)





# PUSH(info)

# x = OUT(info)

# ret = []

# for i in range(len(x)):
# 	ret.append(x[i][3])

# # # name = info.first + '.gif'

# # # print(ret)
# for i in range(len(x)):
# 	name = x[i][0] + '.gif'
# 	with open(name , 'wb') as w :
# 		w.write(ret[i])
# 	render(x[i][0] , x[i][1] , x[i][2] , name)

