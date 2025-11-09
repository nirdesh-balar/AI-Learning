def sum (n):
    if(n==1):
        return 1
    return sum(n-1)+n 

print(sum (4))

se=[2,4,5,"d","g"]
idx=0
def Pri(se,idx):
    if(idx==len(se)):
        return
    print(se[idx])
    Pri(se,idx+1)

Pri(se,idx)

    
    