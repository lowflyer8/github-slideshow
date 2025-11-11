class studentnode:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks
        self.next = None      
        
class studentlinkedlist:
    def __init__(self):
        self.head = None
        
    def addstudent(self , rollno , name ,marks):
        newnode = studentnode(rollno , name ,marks)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
        print("?. student record added.")
        
    def deletestudent(self, rollno):
        current = self.head
        prev = None
        while current:
            if current.rollno == rollno:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print("?. student record deleted")
                return
            prev = current
            current = current.next
        print("?.? student not found")
        
    def updatestudent(self, rollno , newname , newmarks):
        current = self.head
        while current:
            if current.rollno == rollno:
                current.name = newname
                current.marks = newmarks
                print("?. student record updated.")
                return
            current = current.next
        print("??. student not found.")
        
    def displaystudents(self,sortby="rollno", ascending=True):
        student = []
        current = self.head
        while current:
            student.append((current.rollno,current.name,current.marks))
            current = current.next
            
        if sortby == "rollno" :
            student.sort(key=lambda x: x[0], reverse=not ascending)
        elif sortby == "marks":
            student.sort(key=lambda x: x[2],reverse=not ascending)
            
        if not student:
            print("? no records to display.")
            return
        
        print("? student reocrds:")
        for s in student:
            print(s)
            
    def searchstudent(self,rollno):
        current = self.head
        while current:
            if current.rollno == rollno:
                print(f"student found: rollno: {current.rollno},name:{current.name}, marks: {current.marks}")
                return
            current = current.next
        print("student not found")
        
def menu():
    system = studentlinkedlist()
    while True:
        print("\n---student reocrd managment menu---")
        print("1. add student")
        print("2. delete student")
        print("3. update student")
        print("4. search student")
        print("5. display all students")
        print("6. exit")
        
        choice = input("enter your choice(1-6):")
        
        if choice == '1':
            roll = int(input("enter roll no:"))
            name = input("enter name:")
            marks = int(input("enter marks:"))
            system.addstudent(roll,name,marks)
            
        elif choice == '2' :
            roll = int(input("enter roll no to delete:"))
            system.deletestudent(roll)
            
        elif choice == '3':
            roll = int(input("enter roll no to update:"))
            name = input("enter new name:")
            marks = int(input("enter new marks:"))
            system.updatestudent(roll,name,marks)
            
        elif choice == '4':
            roll = int(input("enter roll no to search:"))
            system.searchstudent(roll)
            
        elif choice == '5':
            sortkey = input("sort by 'rollno' or 'marks':").strip()
            order = input("order 'asc' or 'desc':").strip()
            ascending = True if order == 'asc' else False
            system.displaystudents(sortby=sortkey, ascending=ascending)
            
        elif choice == '6':
            print("exiting student record managment system.")
            break
        
        else:
            print("invalid choice try again")
            
menu()