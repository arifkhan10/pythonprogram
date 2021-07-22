n1=int(input("enter the number"))
n2=int(input("enter the number"))
n3=int(input("enter the number"))
list2=[n1,n2,n3]
def sqr(x):
    return x**2
print(list(map(sqr,list2)))    
