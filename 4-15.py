from pandas import Series, DataFrame
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

r_data = {'City':['서울', '대구', '부산', '대전'], 'Total1':[55000,49000,52000,50000],'Total2':[65000,59000,62000,60000]}
#print(type(r_data))
i_data = ['one','two','three','four']

#print(r_data)
#print(i_data)

d_frame = DataFrame(r_data, index=i_data)
#print(type(d_frame))
#print(d_frame)
#print(d_frame.index)
#print(d_frame.values)
#print(d_frame['City'])
#print(d_frame.ix['one'])

for e in d_frame.values:
    #print(e)
    for i,z in enumerate(e):
        print(i,z)
