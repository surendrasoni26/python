digits="0123456789"

list = [1, 2, "three", "four"]

for i in list:
    #a=i.strip(" ")
    print (i)

print ("============")
print("====")
print("====")
print (list[2])

list1=list.append("five")
print (list)
print (list1)
list.append("six")
print (list)
list.pop()
print(list)

print ("++++++++++++++++")

def test():
    for item in range(1,10):
        if (item==5):
            print("inside if block")
            print("item value is "+ str(item))
        else:
            print("inside else block")
            print("item value is "+ str(item))
            #break
            continue
            count=0
            count += item
            print(count)
test()
