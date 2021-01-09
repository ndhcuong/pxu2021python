from Model import Person
import View

#Hàm in ra tất cả dữ liệu
def showAll():
   #Lấy danh sách các Person
   people_in_db = Person.get_All_Person()
   #calls view
   View.showAllView(people_in_db)

#Hàm tương tác với người dùng
def start():
   choice = View.startView()
   if choice == 'y':
      showAll()
   else:
      View.endView()

#Chương trình chính
if __name__ == "__main__":
   #running controller function
   start()