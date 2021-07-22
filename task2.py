n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
large=[]

small=[]

def myMax(n1,n2):

    if n1>n2:

        large.append(n1) 

        small.append(n2)   

    else:

        small.append(n1)

        large.append(n2)  

    return large,small

print(myMax(n1,int(input("enter the second number"))))          

