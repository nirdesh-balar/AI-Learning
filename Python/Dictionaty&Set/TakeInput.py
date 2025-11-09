marks = {}

a = int (input("Phy : "))
b = int (input("Chm : "))
c = int (input("Math : "))

marks.update({"Phy":a})
marks.update({"Chm":b})
marks.update({"Math":c})

print(marks)