import sqlalchemy as db

#Thiết lập engine
engine = db.create_engine("mysql://root:@Dmin1234@localhost/qlsv", echo=False)

#Kết nối tới csdl
connection = engine.connect()
metadata = db.MetaData()
person = db.Table('person', metadata, autoload = True, autoload_with = engine)

#Cú pháp update
#db.update(table_name).values(attribute = new_value).where(condition)
query_insert = db.update(person).values(name='JOE').where(person.columns.personID == 23)
ResultProxy = connection.execute(query_insert)

#In kết quả ra màn hình
query_select = db.select([person])
ResultProxy = connection.execute(query_select)
ResultSet = ResultProxy.fetchall()
#In kết quả ra màn hình
for item in ResultSet:
    print(item)

#Đóng kết nối
ResultProxy.close()