'''
Q2: Given an array of integers and a number k, the task is to find the number of pairs of integers in the array whose sum is equal
value 'k'. output the number of all the ** unique ** pairs that sum up to specific value 'k'.
input:
array=[1,3,2,2]
k=4

output:
2
'''
def findpair(array,k):
    i=0
    for i in range(len(array)):
        if array[i] + array[i+1] == k:
            return array[i], array[i+1]
            #i=i+1
            #continue
        else:
            return "No pair found"
        #i=i+1
        #continue

array=[1,3,2,2]
k=4
Pair=findpair(array,k)

print ("Pair is :", Pair)

print ("######## 2nd try: Differnt way #########")

def findpair(array,k):
    i=0
    count=0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == k:
                print(array[i], array[j])
                count+=1

    return count

array=[1,3,2,2]
k=4
Pair=findpair(array,k)

print ("Pair is :", Pair)
