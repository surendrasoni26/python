"""
Q1: You have been given a list of intergers and you have been asked to reverse the last n elements of the list only
ex:
input:
list1=[1,2,3,4,5,6,7,8,9]
n=4
Output:
list1=[1,2,3,4,5,9,8,7,6]
"""
list1=[1,2,3,4,5,6,7,8,9]
n=4
list2=[]
#1st way to reverse a list
# Testing reverse() method
list1.reverse()
#Testing Appending to another list
list2.append(list1)

#Testing another way of assigining one string to another/new string "Note, did not Initialize list3 here as I did for list2 above"
list3=list1
print (list2)
print (list1)
print ('I am the 3rd list ' +str(list3)) #with concatenate option, you need to convert list to string
print ('I am the 3rd list without concatenate: ', list3) #without concatenate option
print (list1[:4])
print (list1[5:])

#2nd way to reverse a list Using slicing operation

list4=list1[::-1]
print (list4)

## Solution for original question asked at start
## Using slicing operation (other than reverse method)
print ("**** original Question Solution ****")
print (" ")
print ("original list is: ", list4)

#To print only subset of list, with reversed output
list4=list4[(n+1):][::-1]
print ("reversed subset of list up to n=4 is: ", list4)

#To print complete list, with reversed output
list4[(n+1):]=list4[(n+1):][::-1]

print ("reversed list up to n=4 is: ", list4)
