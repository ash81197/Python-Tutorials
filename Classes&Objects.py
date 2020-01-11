class student:
    def __init__(self,id):
        self.id=id
        print("Class has been Created...")
    def __del__(self):
        print("ID:",self.id,"\nClass has been destroyed...")
    def input(self,name,rollno):
        #print("Please enter your name: ")
        self.name=name
        #print("Please enter your roll no: ")
        self.rollno=rollno
    def output(self):
        print("Hello",self.name)
        print("Your Roll no is:",self.rollno)
obj=student(6)
obj.input("Aashish Gupta",101)
obj.output()
obj.__del__()
