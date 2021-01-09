class Person:
    # Thuộc tính có thể khơi tạo mặc định hoặc để trống
    nationality = "Việt Nam"

    # Phương thức khởi tạo
    def __init__(self, name, age):
        # Khởi tạo thuộc tính của lớp ngay trong hàm init
        self.name = name
        self.age = age

    # Thiết lập giá trị cho thuộc tính
    def set_nationality(self, nationality):
        self.nationality = nationality

    # Lấy thông tin của đối tượng
    def __str__(self):
        return "{} có tuổi là {} và quốc tịch là {}".format(self.name, self.age, self.nationality)

    @classmethod
    #Phương thức giả định lấy dữ liệu
    def get_All_Person(self):
        database = [("Nam", 12), ("Hung", 23), ("Nhi", 16), ("Quyen", 18), ("Thao", 20)]
        result = []  #Trả về kết quả là list gồm các đối tượng Person
        #Chuyển database ở trên thành các đối tượng Person - tương tự việc lấy trong CSDL sau này
        for idx, (name, age) in enumerate(database):
            tam = Person(name, age)
            result.append(tam)
        return result