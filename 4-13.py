import pandas as pd

df = pd.read_excel('c:/Atom/section4/excel_s1.xlsx', header=0)
#print(df)

#print(df['State'])
#df['State'] = df['State'].str.replace(' ','|')
#print(df)

df['Avg'] = df[['2003', '2004', '2005']].mean(axis=1)
#print(df)

df['Sum'] = df[['2003', '2004', '2005']].sum(axis=1)
#print(df)

#print(df[['2003', '2004', '2005']].max(axis=1))
#print(df[['2003', '2004', '2005']].max(axis=0))
#print(df[['2003', '2004', '2005']].min(axis=1))
#print(df[['2003', '2004', '2005']].min(axis=0))

#print(df.describe())

#df.to_excel('c:/Atom/section4/result_s1.xlsx')
df.to_excel('c:/Atom/section4/result_s1.xlsx', index=None)
