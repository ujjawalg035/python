#to check the eligibility of ncc
G=input("enter your gender:")
age=int(input("enter your age"))
h=float(input("enter your height"))
w=float(input("enter your weight"))
if G=='m':
    if age>18 and h>5.8 and w>60:
        print("eligible")
    else:
        print("not eligible")
elif G=='f':
    if age>18 and h>5.4 and w>55:
        print("eligible")
    else:
        print("not eligible")
else:
    print("not any gender")
