target = "learning"
with open("first.txt","r") as f:
    data = f.read()
    if(data.find(target)):
        print("Found")
    else:
        print("Not Found")