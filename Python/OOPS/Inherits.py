class Empployee:

    def __init__(self,role,name,salary):
        self.role = role
        self.name = name
        self.salary = salary

    def showDetail(self):
        print(self.role)
        print(self.name)
        print(self.salary)

class Engineer(Empployee):

     def __init__(self, age , dep):
         self.age=age
         self.dep = dep
         super().__init__("Engineer","manoj","60,000")
         

p1=Engineer(40,"Management")
p1.showDetail()
        
