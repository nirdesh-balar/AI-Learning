# split number form "." as a integer and fractional part 

a = input("Enter Nunmber = ")

if "." in a :
    integer , fractional = a.split(".")
else :
    integer = a
    fractional = "."

print("Integer = ",integer)
print(f"Fractional = .{fractional}")