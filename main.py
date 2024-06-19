import pandas as pd

cs = {
  "collg": ["C1","C1","C1","C1","C1","C1"],
  "name": ["Roshan", "Roshan", "Roshan", "Tharun","Tharun","Tharun"],
  "Branch": ["CS1","CS1","CS1","S","S","S"],
  "Subject": ["M1","M2","OS","M1","M2","OS"],
  "Marks": [40,30,55,55,35,45]
}

phy = {
  "collg": ["C1","C1"],
  "name": ["Roshan","Tharun"],
  "Branch": ["CS","CS"],
  "Subject": ["P","P"],
  "Marks": [40, 30]

}

che = {
  "collg": ["C1","C1","C1","C1","C1"],
  "name": ["Roshan","Tharun","Tharun","Tharun","Tharun"],
  "Branch": ["CS","CS","CS","CS","CS"],
  "Subject": ["C","C","C","C","N"],
  "Marks": [35, 30, 20, 10, 5]

}

df1 = pd.DataFrame(cs)
new_df = df1["Branch"].str.find("CS")
print("-1")



df2 = pd.DataFrame(phy)
df3 = pd.DataFrame(che)

df3 =  df3.groupby(by=["name","Subject"],as_index=False).sum(["Marks"])
print(df1)
# print(df2)
# print(df3)

merged=pd.concat([df1,df2,df3],ignore_index=True,axis=0)
G=merged.groupby('name',as_index=False)
Total=G['Marks'].sum()
count=(G['Marks'].count())
print(count)
print(Total)
print(type(Total))
print(Total['Marks'].div(5))
# print(percent)
# print(type(percent))

# for name,df in grouped:
#   t1=grouped.get_group(name)
#   print(name)
#   print(t1)
#   total=t1['Marks'].agg("sum")
#   print("Total",total)
#   count=t1['Marks'].count()
#   percentage=total/(count)
#   print("percentage=",percentage)
#   print("/////////////////")

# print(merged)
