from __future__ import with_statement
from collections import defaultdict

file = open('/Users/parshvadaftari/Codefest_2/algo1/TWSP_small.txt','r')

tdata = list(file.read().split('\n'))
data=[]
#print(tdata)

for i in range(1,len(tdata)):
    temp = list([int(j) for j in tdata[i][0:len(tdata[i])].split()])
    data.append(temp)

dict1 = defaultdict(lambda: [])
for i in data:
    dict1[i[0]].append(i[1:])

myKeys = list(dict1.keys())
myKeys.sort()
sorted_dict = {i: dict1[i] for i in myKeys}

# myValues = list(sorted_dict.values())
# for i in range(0,len(myValues)):
#     myValues[i].sort(reverse=True)

for i in sorted_dict:
    sorted_dict[i].sort(reverse=True)



with open('output_small.txt', 'w') as f:
    for i in sorted_dict:
        for j in sorted_dict[i]:
            f.write(str([i] + j)+'\n')

# for i in sorted_dict:
#     for j in sorted_dict[i]:
#         print([i] + j)

#print(sorted_dict)
