import db_exceptions
import person_db

class PersonView(object):

    #Hàm hiển thị tất cả dữ liệu về person
    def display_all_person(self, items):
        print("Dữ liệu về các person thu được như sau:")
        for item in items:
            print("ID: {}, họ và tên: {}, tuổi: {}".format(item.personID, item.name, item.age))
        print("-----Kết thúc hiển thị dữ liệu------")
