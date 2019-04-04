import pandas as pd
import numpy as np

#랜덤으로 dataframe 생성
#df = pd.DataFrame(np.random.randint(0,100, size=(100, 4)), columns=['ONE','TWO','THREE','FOUR'])
df = pd.DataFrame(np.random.randn(100,4), columns=['ONE','TWO','THREE','FOUR'])

print(df)

#df.to_csv('c:/Atom/section4/result_s2.csv', index=False)
df.to_csv('c:/Atom/section4/result_s2.csv', index=False, header=False)
