import db_exceptions
import person_db

class PersonView(object):

    #Hàm hiển thị tất cả dữ liệu về person
    def display_all_person(self, items):
        print("Dữ liệu về các person thu được như sau:")
        for item in items:
            print("ID: {}, họ và tên: {}, tuổi: {}".format(item.personID, item.name, item.age))
        print("-----Kết thúc hiển thị dữ liệu------")

    #Hàm thông báo kết quả insert
    def ket_qua_insert(self, resultID):
        id = resultID[0]
        if id > 0:
            print("Insert thanh cong")
        else:
            print("Fail")

    def thong_bao_loi(self, err_msg):
        print('-'*30)
        print(err_msg)
        print('-'*30)