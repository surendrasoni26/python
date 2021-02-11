
#numbers=[1,2,3]
def even_chk(number):
    result = number % 2 == 0
    return result

print ("Calling function 1nd time")
print(even_chk(21))
print ("Calling function 2nd time")
print(even_chk(22))
#################
def even_chk_list(numbers):

    for number in numbers:
        if number % 2 == 0:
            return True
        else:
            pass
    return False

print ("Calling function 1nd time")
print(even_chk_list([21,22,23]))
print ("Calling function 2nd time")
print(even_chk_list([24,21,23]))
