#Method1
#to read all lines
with open("learning_python.txt") as file_object:
    content=file_object.read()
print(content)

print("##############")
#to read line by lines as list
with open("learning_python.txt") as file_object:
    content=file_object.readlines()
print(content)

print("##############")
#another way of reading file line by line
filename='learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
print("##############")
#replacing a word using python... here replacing pyhton with java
filename='learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        new_data=line.replace('python', 'java')
        print(new_data)

print("##############")
#Method 2

myfile=open('learning_python.txt')
file_data=myfile.read()
print(file_data)
