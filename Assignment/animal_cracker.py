#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#Option 1 if 2 separate strings given
def animal_cracker(a,b):
    if a[0] == b[0]:
        return True
    else:
        return False

#CHECK
result=animal_cracker('Nature', 'Natural')
print(result)
#CHECK2
result1=animal_cracker('India', 'America')
print (result1)

#Option 2 if 2 words present in 1 string

def animal_cracker2(word):
    word_list=word.split()
    return word_list[0][0] == word_list[1][0]
#        return True
#    else:
#        return False
result=animal_cracker2('Nature Natural')
print(result)
#CHECK2
result1=animal_cracker2('India America')
print (result1)
