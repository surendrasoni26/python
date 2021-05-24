#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(a,b):
    if a+b == 20 or a == 20 or b == 20:
        return True
    else:
        return False

#CHECK
result=makes_twenty(9,11)
print(result)
#CHECK2
result1=makes_twenty(1,20)
print(result1)
#CHECK3
result2=makes_twenty(2,3)
print(result2)
