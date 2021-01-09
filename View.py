from Model import Person

def startView():
    print('Ví dụ về mô hình MVC - dạng đơn giản nhất')
    key = input('Bạn có muốn xem tất cả dữ liệu không? [y/n] ')
    return key

def endView():
    print('See You')

def showAllView(danhsach):
    for person in danhsach:
        print(person.name, '--', person.age)
    print('Tổng cộng có ', len(danhsach), ' person')