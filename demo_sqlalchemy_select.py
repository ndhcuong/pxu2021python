import sqlalchemy as db

#Thiết lập engine
engine = db.create_engine("mysql://root:@Dmin1234@localhost/qlsv", echo=True)

#Kết nối tới csdl
connection = engine.connect()
metadata = db.MetaData()
#Lấy đối tượng person từ bảng person trong csdl
person = db.Table('person', metadata, autoload = True, autoload_with = engine)

#Lấy tất cả dữ liệu của bảng person - tương đương câu lênh SELECT * FROM person
query = db.select([person])

ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
#In kết quả ra màn hình
for item in ResultSet:
    print(item)

#Đóng kết nối
ResultProxy.close()