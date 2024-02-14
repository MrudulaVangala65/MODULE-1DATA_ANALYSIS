#pandas
import pandas as pd
a=["ram",'raj','mrudula','rishi','yamini','ishu','parvathi']
r=pd.Series(a,index=[1,2,3,4,5,6,7])
print(r)

df=pd.read_csv("/content/pythontextfile1.txt",sep=" ")
print(df)

df=pd.read_csv("/content/pythontextfile1.txt",sep=" ")
print(df)

df1=pd.read_csv("/content/Player.csv")
print(df1)

df1.head()
df1.tail()

df1.shape
d1_lastlines=df1.tail(10)
d1_lastlines=df1.to_csv("manualtesting")

df1=pd.read_csv("/content/Player.csv")
d1_lastlines=df1.tail(10)
d1_firstlines=df1.head(10)
data_manualtesting=pd.concat([d1_lastlines,d1_firstlines],axis=0)
data_manualtesting.to_csv("cancatinated_manualtesting")
rr=pd.read_csv("/content/cancatinated_manualtesting")
print(rr)
print(rr.groupby(['Player_Name'])['DOB'].count())

df1=pd.read_csv("/content/Player.csv")
print(df1)
df1.shape
df1["class"]=1

import pandas as pd
df=pd.read_excel("/content/newxlsheet.xlsx")
print(df)

print(df.loc[1])

mv=df['rollnumber'].mean()
df=df.fillna(mv)
print(df)

df=df.drop_duplicates()
print(df)

