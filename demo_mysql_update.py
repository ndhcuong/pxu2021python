import mysql.connector

#Kết nối đến csdl sakila
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "@Dmin1234",
    database = "qlsv"
)

mycursor = mydb.cursor()

#Cập nhật dữ liệu
sql = """ UPDATE person
                SET name = %s
                WHERE personID = %s """
val = ("Duc", "2")

mycursor.execute(sql, val)
mydb.commit()

print('Finished')

mycursor.close()
mydb.close()