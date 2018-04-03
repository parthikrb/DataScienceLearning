import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan], 'B':[6,np.nan,np.nan], 'C':[8,5,0]}
df = pd.DataFrame(d)
print(df)
print('*%' *20)
print('*%' *20)
print(df.dropna())
print('*%' *20)
print('*%' *20)
print(df.dropna(thresh=2))
print('*%' *20)
print('*%' *20)
print(df.dropna(axis=1))
print('*%' *20)
print('*%' *20)
print(df.fillna('Fill'))
print('*%' *20)
print('*%' *20)
print(df['A'].fillna(df['A'].mean()))