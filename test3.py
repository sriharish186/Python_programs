import pandas as pd
import numpy as np
df2= pd.read_csv("NFL_Play_by_Play_2009-2016.csv")
print(df2)
#print(df2.to_string()) # jupyter
#print(df2.describe(include=object)) # summary statistics
#rprint(type(df2))
#print(df2["Date"][0])
#print(df2.head())
#print(df2.tail(10))
#print(df2.loc[df2["Drive"]==1]) #where(Date==4&) group
#print(len(df2))

"""numbers = np.linspace(1, 100, 50) #spacing =101/50
#print(numbers)
#print(numbers.reshape(-1,2))
numbers=np.linspace(1,50,24,dtype=int)
print(numbers)
mask= numbers%4==0
mask = numbers > 20 
A=np.linspace(1,33,2).reshape(16,1)
B=np.linspace(1,49,1).reshape(16,3)
print(A+B)
A=np.linspace(1,6,6).reshape(3,2)
B=np.linspace(2,4,2).reshape(2,1)
print(A@B)"""


