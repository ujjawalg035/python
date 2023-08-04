p=int(input("enter your marks of physics"))
c=int(input("enter your marks of chemistry:"))
b=int(input("enter your marks of biology:"))
m=int(input("enter your marks of mathematics:"))
c=int(input("enter your marks of computer:"))
s=p+c+b+m+c
per=s/5
print("percentage:",per)
if per>=90:
    print("Grade A")
elif per>=80:
    print("Grade B")
elif per>=70:
    print("Grade C")
elif per>=60:
    print("Grade D")
elif per>=40:
    print("Grade E")
else:
    print("Grade F")
    

