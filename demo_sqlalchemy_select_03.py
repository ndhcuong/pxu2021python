import sqlalchemy as db

#Thiết lập engine
engine = db.create_engine("mysql://root:@Dmin1234@localhost/sakila", echo=False)

#Kết nối tới csdl
connection = engine.connect()
metadata = db.MetaData()
actor = db.Table('actor', metadata, autoload = True, autoload_with = engine)

#Lọc dữ liệu SELECT * FROM actor WHERE first_name = 'Joe'
query = db.select([actor]).where(actor.columns.first_name == 'Joe')

ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
#In kết quả ra màn hình
for item in ResultSet:
    print(item)

#Đóng kết nối
ResultProxy.close()