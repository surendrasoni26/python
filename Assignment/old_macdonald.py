#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(word):
    if len(word)>3:
        return word[:3].capitalize() + word[3:].capitalize()
    else:
        return "name is too short!!"
#CHECK
result=old_macdonald('surendra')
print (result)

#option 2

def old_macdonald2(word):
    if len(word)>3:
        return word[0].upper() + word[3].upper()
    else:
        return "name is too short!!"
#CHECK2
result1=old_macdonald2('surendra')
print (result1)
