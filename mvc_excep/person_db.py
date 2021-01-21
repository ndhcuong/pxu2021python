import sqlalchemy as db
import db_exceptions

#Xây dựng hàm thiết lập kết nối đến csdl
#Trả về đối tượng là connection, metadata và engine
def ket_noi_den_csdl(database_server, username, password, database):
    try:
        connection_str = "mysql://{}:{}@{}/{}".format(username, password, database_server, database)
        engine = db.create_engine(connection_str)
        connection = engine.connect()
        metadata = db.MetaData()
        return connection, metadata, engine
    except:
        raise db_exceptions.DatabaseConnection("Thông tin kết nối username = {}, pass = {}, "
                                               "database = {} hoặc server ={} không đúng".format(username,
                                                                                                 password,
                                                                                                 database,
                                                                                                 database_server))


#Xây dựng hàm lấy tất cả dữ liệu của bảng Person
def lay_tat_ca_du_lieu_bang_person(connection, metadata, engine):
    try:
        # Lấy đối tượng person từ bảng person trong csdl
        #person = db.Table('person', metadata, autoload=True, autoload_with=engine)
        person = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)

        # Lấy tất cả dữ liệu của bảng person - tương đương câu lênh SELECT * FROM person
        query = db.select([person])

        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()

        return ResultSet
    except:
        raise  db_exceptions.SelectError("Xảy ra lỗi trong quá trình thực hiện lấy dữ liệu")

#Hàm insert - tra ve id vua duoc tao - hãy xử lý lỗi trong quá trình insert
def them_person(connection, metadata, engine,
                name, age):
    # Lấy đối tượng person từ bảng person trong csdl
    person = db.Table('person', metadata, autoload=True, autoload_with=engine)
    # Chèn 1 dòng vào bảng person
    query = db.insert(person).values(name=name, age=age)
    ResultProxy = connection.execute(query)
    # Trả về giá trị id vừa được sinh
    return ResultProxy.inserted_primary_key

#Hàm update


#Hàm delete

