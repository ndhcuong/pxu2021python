import mysql.connector

#Kết nối đến csdl qlsv
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "@Dmin1234",
    database = "qlsv"
)

#Liệt kê các bảng dữ liệu trong csdl sakila
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for item in mycursor:
    print(item)

#Chèn dữ liệu vào bảng person
sql = "INSERT INTO person (name, age) VALUES (%s, %s)"
val = ("Long", "21")
mycursor.execute(sql, val)

mydb.commit()

#Lấy id vừa được sinh ra (do personID được sinh tự động)
if mycursor.lastrowid:
    print('ID của person vừa được tạo là ', mycursor.lastrowid)
else:
    print('Không tìm thấy ID của record vừa được tạo')

mydb.close()