import numpy as np # alias
import pandas as pd
l=[1,2,3]
list1=[[1,2],[2,2],[2,3],["hi",True]]
#print(list1)
#print(list1[0][1])
arr1=np.array(list1)
#print(arr1)
temperatures = np.array([29.3, 42.1, 18.8, 16.1, 38.0, 12.5, 12.6, 49.9, 38.6, 31.3, 9.2, 22.2]).reshape([2,2,3])
#np.swapaxes(temperatures, 1, 2)
#print(np.swapaxes(temperatures, 0, 2)) 
temperatures = np.swapaxes(temperatures, 0, 2)
#print(temperatures)

# dataframes
dict1={"fruit":["apple","guava"],"price":[25,35],"qty":[4,2]}
df1 =pd.DataFrame(dict1,index=[1,2])
#print(df1["price"][2]) #fib series -0,1,1,2,3,5,8,13 even no, 0,2,4,6,.....100
#print(df1.price[2])

dict1={"hat":"apple",2:"da",3:"gg",3:"hh"}
s1=pd.Series(dict1) # cross bw list & dict
print(s1[2])

df2= pd.read_csv("NFL_Play_by_Play_2009-2016.csv")
print(df2.describe())
