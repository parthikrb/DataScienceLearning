import numpy as np
import pandas as pd

label = ['a', 'b', 'c']
my_data = np.array([10, 20, 30])
d = {'a' : 10, 'b' : 20, 'c' : 30}


print(pd.Series(data = my_data))
print('*#'*20)
print(pd.Series(data= my_data, index= label))
print('*#'*20)
print(pd.Series(d))
print('*#'*20)

ser1 = pd.Series([1,2,5,4], ['USA', 'India', 'China', 'Japan'])
print(ser1)
print('*#'*20)

ser2 = pd.Series([2,5,7,4], ['India', 'USA', 'Singapore', 'China'])
print(ser2)
print('*#'*20)

print(ser1 + ser2)