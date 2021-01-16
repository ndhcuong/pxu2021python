import sqlalchemy as db

#Thiết lập engine
engine = db.create_engine("mysql://root:@Dmin1234@localhost/qlsvpxu", echo=True)

#Kết nối tới csdl
connection = engine.connect()
metadata = db.MetaData()
sinhvien = db.Table('sinhvien', metadata, autoload = True, autoload_with = engine)

#Liệt kê các cột của bảng sinhvien
print(sinhvien.columns.keys())

#In metadata của bảng sinhvien
print(repr(metadata.tables['sinhvien']))

