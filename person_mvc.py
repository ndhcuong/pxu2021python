import db_exceptions
import person_db
import person_model, person_view, person_controller

def start():
    #Khởi tạo đối tượng model
    model = person_model.PersonModel("localhost", "root", "@Dmin1234", "qlsv")
    #Khởi tạo đối tượng view
    view = person_view.PersonView()
    #Khởi tạo controller
    controller = person_controller.PersonController(model, view)

    #Hiển thị tất cả dữ liệu của bảng person
    controller.show_all_person()

if __name__ == "__main__":
    start()