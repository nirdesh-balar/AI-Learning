class student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    @staticmethod       # We can not need to declear "self" in method . it is made staticmethod 
    def hello():
        print("Hello")


    def avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print(self.name , "your avg = " ,sum/3)
        
s1 = student("nirdesh",[45,35,46])
s1.hello()
s1.avg()