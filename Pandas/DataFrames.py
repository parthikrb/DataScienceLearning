import numpy as np
import pandas as pd
from numpy.random import randn

# np.random.seed(101)

dataf = pd.DataFrame(randn(5,4), ['x','y','z','a','b'], ['c','d','e','f'])
print(dataf)
print('*#'*20)
print(dataf['c'])
print('*#'*20)
print(dataf[['c','f']])
print('Create New Column')
dataf['new'] = dataf['d'] + dataf['f']
print(dataf)
print('Delete the Column')
print('Axis 1 indicates the Column')
print(dataf.drop('new', axis=1))
print(dataf)

#Selection of Rows in DataFrame
print('*#'*20)
print('*#'*20)
print(dataf.loc['z'])

#Selection of Row based on index
print('*#'*20)
print('*#'*20)
print(dataf.iloc[[2,3]])

#Selection of subset i.e., using row and column
print('*#'*20)
print('*#'*20)
print(dataf.loc['z', 'd'])

print('*%' *20)
print('*%' *20)
print(dataf[dataf>0])

print('*%' *20)
print('*%' *20)
print(dataf[dataf['c']>0][['e', 'd']])

print('*%' *20)
print("Multiple Conditions --> use & instead of 'and'")
print('*%' *20)
print(dataf[(dataf['c']>0) & (dataf['new']<1)])

print('*%' *20)
print("Multiple Conditions --> use | instead of 'or'")
print('*%' *20)
print(dataf[(dataf['c']>0) | (dataf['new']<1)])

print('#@$' *20)
print('SET INDEX')
print('@#%' *20)
newindex = 'CA NY WY OR CO'.split()
dataf['STATES'] = newindex
print(dataf.set_index('STATES'))