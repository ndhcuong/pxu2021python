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
        item = menu()
        while item in ["1", "2", "3", "4"]:
            if item == "1":
                controller.show_all_person()
            elif item == "2":
                hoten = input("Nhập họ tên: ")
                tuoi = int(input("Nhập tuổi: "))
                controller.them_person(hoten, tuoi)

            item = menu()

    except db_exceptions.DatabaseConnection as err:
        print(err)

def menu():
    print("1: Hiển thị tất cả Person")
    print("2: Thêm mới Person")
    print("3: Cập nhật Person")
    print("4: Xóa Person")
    choice = input("Bạn hãy chọn các số từ 1 đến 4. Ngược lại là thoát khỏi chương trình.")
    return choice

if __name__ == "__main__":
    start()