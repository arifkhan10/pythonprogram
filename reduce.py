from functools import reduce
num=[2,3,4,5,6]
evens=list(filter(lambda n :n%2==0,num))
doubles=list(map(lambda n:n*2,evens))
print(doubles)
x=reduce(lambda x,y:x+y,num)
print(x)