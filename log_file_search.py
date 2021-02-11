
Elastic_Slow_Log = r"G:\Git\python\elasticsearch_index_search_slowlog1.log"
Elastic_ResTime = []

phraes_to_check=["took"]

with open(Elastic_Slow_Log) as f:
	f = f.readlines()

for line in f:
	for phrase in phraes_to_check:
		if phrase in line:
			Elastic_ResTime.append(line)
			break


print (Elastic_ResTime)
print(Elastic_ResTime[0])
size = len(Elastic_ResTime)
print(size)
print('##############')

for i in range(0, size):
	time=[]
	a=Elastic_ResTime[i].lstrip("took")
	b=a.rstrip("took")
	time.append(b)

print(time)



