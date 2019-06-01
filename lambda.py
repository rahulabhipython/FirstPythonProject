from functools import reduce
nums = [1,2,3,4,5,6,7,8]

double = reduce(lambda a,b: a+b,list(map(lambda y : y*2, list(filter(lambda x : x%2==0,nums)))))
print(double)