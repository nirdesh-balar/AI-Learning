#  Write a function that takes two integers a and b and print all even numbers between them (inclusive).

a = int(input("Enter your first num ="))
b = int(input("Enter your second num = "))

def even(a,b):
    i = a
    while i<=b:
        if i%2==0:
            print(i)
        i += 1
    
print(even(a,b))  

