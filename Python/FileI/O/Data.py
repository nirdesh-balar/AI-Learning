with open("first.txt","r") as f:
  data = f.read()

New = data.replace("python","java")
print(New)

with open("first.txt","w") as f:
  data = f.write(New)