n=input("enter your name:")
r=int(input("enter your roll no.:"))
s=input("enter your semester:")
a=float(input("enter your attendance:"))
if(a>=75.0):
    e=float(input("enter your marks of english:"))
    c=float(input("enter your marks of chemistry:"))
    ele=float(input("enter your marks of electronics:"))
    py=float(input("enter your marks of python:"))
    m=float(input("enter your marks of maths:"))
    sum=e+c+ele+py+m
    frac=sum/500
    p=frac*100
    print("percentage=",p)
    if(p in range(91,101)):
        print("grade=A+")
    elif(p in range(86,91)):
        print("grade=A")
    elif(p in range(76,86)):
        print("grade=B+")
    elif(p in range(66,76)):
        print("grade=B")
    elif(p in range(50,66)):
        print("grade=C")
    else:
        print("fail")
else:
    print("due to lack of attendence you are detained")
    
            
