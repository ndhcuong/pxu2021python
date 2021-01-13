import mysql.connector

#Kết nối đến csdl sakila
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "@Dmin1234",
    database = "qlsv"
)


mycursor = mydb.cursor()

#Lấy tất cả dữ liệu trong bảng person
sql = "SELECT * FROM person"
mycursor.execute(sql)

my_result = mycursor.fetchall()

#In kết quả ra màn hình
for item in my_result:
    print(item)

#Câu sql khác
sql = "SELECT name, age FROM person"
mycursor.execute(sql)

my_result = mycursor.fetchall()

#In kết quả ra màn hình
for item in my_result:
    print(item)

#Sự khác biệt giữa fetchall và fetchone
print("Sự khác biệt giữa fetchall và fetchone")
sql = "SELECT name, age FROM person"
mycursor.execute(sql)
my_result = mycursor.fetchone()
print(my_result)

mydb.close()