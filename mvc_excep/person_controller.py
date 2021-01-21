import db_exceptions
import person_db

class PersonController(object):
    #Phương thức khởi tạo
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #Phương thức hiển thị tất cả dữ liệu của bảng person
    def show_all_person(self):
        try:
            items = self.model.get_all_person()
            self.view.display_all_person(items)
        except db_exceptions.SelectError as err_msg:
            self.view.thong_bao_loi(err_msg)

    #Phương thức insert - hãy xử lý lỗi trong quá trình insert
    def them_person(self, name, age):
        resultID = self.model.them_person(name, age)
        self.view.ket_qua_insert(resultID)

    #Phương thức update


    #Phương thức delete