import person_db
import db_exceptions

class PersonModel(object):
    #Phương thức khởi tạo
    def __init__(self, database_server, username, password, database):
        self.connection, self.metadata, self.engine = person_db.ket_noi_den_csdl(database_server,
                                                                                 username,
                                                                                 password,
                                                                                 database)

    #Phương thức lấy dữ liệu
    def get_all_person(self):
        results = person_db.lay_tat_ca_du_lieu_bang_person(self.connection,
                                                           self.metadata,
                                                           self.engine)
        return results

    #Phương thức insert
    def them_person(self, name, age):
        resultID = person_db.them_person(self.connection,
                                       self.metadata,
                                       self.engine,
                                       name, age)
        return resultID

    #Phương thức update

    #Phương thức delete
