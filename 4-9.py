import pandas as pd

#df = pd.read_csv('c:/Atom/section4/csv_s1.csv')
#print(df)

#df = pd.read_csv('c:/Atom/section4/csv_s1.csv', skiprows=[0])
#print(df)

#df = pd.read_csv('c:/Atom/section4/csv_s1.csv', skiprows=[0], header=None)
#print(df)

#df = pd.read_csv('c:/Atom/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014, 2015])
#print(df)

#df = pd.read_csv('c:/Atom/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014, 2015], index_col=[0])
#print(df)

#df = pd.read_csv('c:/Atom/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014, 2015], index_col=[0], na_values=['JAN'])
#print(df)

#df = pd.read_csv('c:/Atom/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014, 2015])
#print(df)
#print(df.index)
#print(list(df.index))
#print(df.index.values.tolist())
#print(df.index.values)
#print(df.rename(index={0:'aa', 1:'bb', 2:'cc'}))
#print(df.rename(index=lambda x:x+1))
#print(df.rename(index=lambda x:x*10))

df2 = pd.read_csv('c:/Atom/section4/csv_s2.csv', sep=';', skiprows=[0], header=None, names=['Name', 'TEST1', 'TEST2', 'TEST3', 'Final', 'Grade'])
#print(df2)

#print(df2['Grade'])
#df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
#print(df2)

df2['Avg'] = df2[['TEST1', 'TEST2', 'TEST3', 'Final']].mean(axis=1)
#print(df2)

df2['Sum'] = df2[['TEST1', 'TEST2', 'TEST3', 'Final']].sum(axis=1)
print(df2)
