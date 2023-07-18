dict1={"123":[25,23,20,24],"124":[25,23,20,24],"123":[25,23,21,24]}
print(dict1["123"][0]+dict1["124"][0]) # informal
l=[25,25,20,21]
print(dict1.keys())
for i in dict1.keys():
    print(dict1[i])