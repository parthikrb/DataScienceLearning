#Multi level indexing
import numpy as np
import pandas as pd
from numpy.random import randn

outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = '1 2 3 1 2 3'.split()
hier_index = list(zip(outside, inside))
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

print('*%' *20)
print('*%' *20)
df = pd.DataFrame(randn(6,2), hier_index,['A', 'B'])
print(df)

print('*%' *20)
print('Set name for Column headers')
print('*%' *20)
print(df.index.names)
print('*%' *20)
df.index.names = ['Groups', 'Num']
print(df)

print('*%' *20)
print('Grab value from the data set')
print('*%' *20)
print(df.loc['G2'].loc['2']['B'])

print('Method to pull row 1 from both the groups')
print(df.xs('2',level='Num'))