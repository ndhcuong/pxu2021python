import sqlalchemy as db

#Thiết lập engine
engine = db.create_engine("mysql://root:@Dmin1234@localhost/qlsv", echo=False)

#Kết nối tới csdl
connection = engine.connect()
metadata = db.MetaData()
person = db.Table('person', metadata, autoload = True, autoload_with = engine)

#Lấy tất cả dữ liệu của bảng sinhvien - tương đương câu lênh SELECT * FROM person
def show_all_person(person, connection):
    query = db.select([person])

    proxy = connection.execute(query)
    rs = proxy.fetchall()
    #In kết quả ra màn hình
    for item in rs:
        print(item)

    #Đóng kết nối
    proxy.close()

#Hiển thị dữ liệu
show_all_person(person, connection)

#Chèn 1 dòng vào bảng person
query = db.insert(person).values(name='Hoang Van Long', age = '20')
ResultProxy = connection.execute(query)
#In ra màn hình giá trị id vừa được sinh
print(ResultProxy.inserted_primary_key)

#Hiển thị dữ liệu
print('---Sau khi INSERT--')
show_all_person(person, connection)

#Chèn nhiều dòng vào bảng person
query = db.insert(person)
values = [{'name': 'Loan', 'age': 19},
          {'name': 'Duc', 'age': 22},
          {'name': 'Lien', 'age': 21}]
ResultProxy = connection.execute(query, values)

#Hiển thị dữ liệu
print('----Batch INSERT-----')
show_all_person(person, connection)

ResultProxy.close()
