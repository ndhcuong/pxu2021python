import sqlalchemy as db
import db_exceptions

#Xây dựng hàm thiết lập kết nối đến csdl
#Trả về đối tượng là connection, metadata và engine
def ket_noi_den_csdl(database_server, username, password, database):
    connection_str = "mysql://{}:{}@{}/{}".format(username, password, database_server, database)
    engine = db.create_engine(connection_str)
    connection = engine.connect()
    metadata = db.MetaData()
    return connection, metadata, engine

#Xây dựng hàm lấy tất cả dữ liệu của bảng Person
def lay_tat_ca_du_lieu_bang_person(connection, metadata, engine):
    # Lấy đối tượng person từ bảng person trong csdl
    person = db.Table('person', metadata, autoload=True, autoload_with=engine)

    # Lấy tất cả dữ liệu của bảng person - tương đương câu lênh SELECT * FROM person
    query = db.select([person])

    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    return ResultSet

#Hàm insert


#Hàm update


#Hàm delete

