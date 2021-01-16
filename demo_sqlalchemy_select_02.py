import sqlalchemy as db

#Thiết lập engine
engine = db.create_engine("mysql://root:@Dmin1234@localhost/sakila", echo=False)

#Kết nối tới csdl
connection = engine.connect()
metadata = db.MetaData()
actor = db.Table('actor', metadata, autoload = True, autoload_with = engine)

#Lấy tất cả dữ liệu của bảng actor - tương đương câu lênh SELECT * FROM actor
query = db.select([actor])

ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
#In kết quả ra màn hình
for item in ResultSet:
    print(item)

#Đóng kết nối
ResultProxy.close()