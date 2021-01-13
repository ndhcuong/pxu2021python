import mysql.connector

#Kết nối đến csdl sakila
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "@Dmin1234",
    database = "qlsv"
)

mycursor = mydb.cursor()

sql = "DELETE FROM person WHERE personID = %s"
val = ("2", )

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, " bảng ghi đã bị xóa")

mycursor.close()
mydb.close()
