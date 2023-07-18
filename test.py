#list1=[[1,2],[2,2],[2,3],["hi",True]] # list vs array 
list1=[1,2,2,2,2,3,"hi",True]
a="harish"
# traversal
for i in list1:
    print(i)
#print(list1[-3]) # indexing starts with 0 
# forward or back -1,-2,
#print(len(4)) # strings, list,etc
list1.append(5)
list1.pop(0) #pop stack  remove a certain index push(4)
#list1.clear() # removes completely
list1.remove(2)
#[2,2,2,3,"hi",true,5]
print(list1.index(2)) # index of a certain value
print(list1)
list1.sum()



# tuples

tup1=(1,2,2,3) # they are immutable
print(tup1.index(1))
for i in tup1:
    print(i)

# dictionary
dict1={"hat":"apple",2:"da",3:"gg",3:"hh"} #key:value key print)i,dict[i]
#print(dict1["hat"])
#dict1[3]="15"
for i,j in enumerate(dict1):
    print(i,j,dict1[j])

"""
import pandas
pandas.DataFrame
pandas.Series
import numpy
numpy.array # 3d
"""
