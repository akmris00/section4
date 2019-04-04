import pandas as pd

df2 = pd.read_csv('c:/Atom/section4/csv_s2.csv', sep=';', skiprows=[0], header=None, names=['Name', 'TEST1', 'TEST2', 'TEST3', 'Final', 'Grade'])
#print(df2)

#print(df2['Grade'])
#df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
#print(df2)

df2['Avg'] = df2[['TEST1', 'TEST2', 'TEST3', 'Final']].mean(axis=1)
#print(df2)

df2['Sum'] = df2[['TEST1', 'TEST2', 'TEST3', 'Final']].sum(axis=1)
print(df2)

#df2.to_csv('c:/Atom/section4/result_s1.csv')
df2.to_csv('c:/Atom/section4/result_s1.csv', index=False)
