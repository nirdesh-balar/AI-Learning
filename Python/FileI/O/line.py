word = "dagd"
data= True
lineNo=1
with open("first.txt","r") as f:
    while data:
        data = f.readline()
        if (word in data):
            print(lineNo)
        lineNo += 1
