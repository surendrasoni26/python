birthdays={'Ramesh':'Apr 1', 'Suresh':'Aug 10', 'Dinesh':'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name=input()
    if name=='':
        break

    if name in birthdays:
        print (birthdays[name]+' is the birthday of'+name)
    else:
        print('i do not have birthday information for '+name)
        print('what is their birthday?')
        bday=input()
        birthdays[name]=bday
        print('Birthday Database Updated.')
print('##########')
for k, v in birthdays.items():
    print('Key: '+k)
    print('Value: '+v)

print('###########')
for i in birthdays.items():
    print (i)
