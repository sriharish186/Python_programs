import pandas as pd

df = pd.read_csv('dirtydata.csv')

print(df)


#df=df.dropna()
#print(df.dropna(inplace=True))
print(df.dropna(axis=1))
print(df.fillna(130, inplace = False))
df["Calories"].fillna(130, inplace = True)
df["Date"].fillna('2020/12/22')
df['Date'] = pd.to_datetime(df['Date'])
print(df.duplicated())