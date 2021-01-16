import sqlalchemy as db

#Thiết lập engine
engine = db.create_engine("mysql://root:@Dmin1234@localhost/qlsv", echo=False)

#Kết nối tới csdl
connection = engine.connect()
metadata = db.MetaData()
person = db.Table('person', metadata, autoload = True, autoload_with = engine)

#Cú pháp delete
#db.delete(table_name).where(condition)
query_delete = db.delete(person).where(person.columns.age > 20)
ResultProxy = connection.execute(query_delete)

#In kết quả ra màn hình
query_select = db.select([person])
ResultProxy = connection.execute(query_select)
ResultSet = ResultProxy.fetchall()
#In kết quả ra màn hình
for item in ResultSet:
    print(item)

#Đóng kết nối
ResultProxy.close()