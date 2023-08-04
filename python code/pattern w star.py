n=int(input("enter your number of rows:"))
for i in range(0,n+1):
    print('*'*i+' '*(2*(n-i)+1)+'*'*i)
print('*'*(2*n+1))
