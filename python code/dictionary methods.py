#my_dict={}
#n=int(input("enter your elements of dictionary:"))
#i=1
#while(i<=n):
#    a=int(input("enter keys:"))
 #   b=int(input("enter your marks:"))
  #  my_dict[a]=b
 #   i=i+1
  #  print("keys are:",a)
   # print("values are:",b)
#print(my_dict)
d1={1:2,3:4,5:6}
d2={"name":"sumit","add":"radhapuram"}
#d1.update(d2)
n=d1.copy()
n.update(d2)
print(n)
