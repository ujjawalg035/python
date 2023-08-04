r=int(input("enter your row"))
for i in range(r+1,0,-1):
    for j in range(1,i+1):
        print("*",end='')
    print(" ")
