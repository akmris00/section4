from pandas import Series

series1 = Series([92600, 94800, 88800, 75400, 92300])
#print(series1)

#print('count', series1.count())
#print('describe', series1.describe())

#print(series1[2])

series2 = Series([92600, 94800,88800, 75400, 92300], index=['2018-02-12','2018-02-13','2018-02-14','2018-02-15','2018-02-16'])
#print(series2)

for date in series2.index:
    print('date', date)

for price in series2.values:
    print('price', price)

series_g1 = Series([10, 20, 30], index=['n1', 'n2', 'n3'])
series_g2 = Series([50, 40, 25], index=['n3', 'n2', 'n1'])

sum = series_g1 + series_g2
mul = series_g1 * series_g2
cul = (series_g1 * series_g2) * (0.5 + 1)
print('sum')
print(sum)
print('mul')
print(mul)
print('cul')
print(cul)
