import db_exceptions
import person_db
import person_model, person_view, person_controller

def start():
    #Khởi tạo đối tượng model
    try:
        model = person_model.PersonModel("localhost", "root", "@Dmin1234", "qlsv")
        #model = person_model.PersonModel("localhost", "root", "admin1234", "qlsv")
        # Khởi tạo đối tượng view
        view = person_view.PersonView()
        # Khởi tạo controller
        controller = person_controller.PersonController(model, view)

        # Them Tuan Anh vao csdl
        #controller.them_person("Tuan Anh", 22)
        # Hiển thị tất cả dữ liệu của bảng person
        controller.show_all_person()
    except db_exceptions.DatabaseConnection as err:
        print(err)




if __name__ == "__main__":
    start()