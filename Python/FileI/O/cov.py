with open("number.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for i in nums:
        if(int(i)%2==0):
            print(i)
            