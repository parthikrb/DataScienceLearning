import numpy as np


list_of_int = [1,2,3,4]
arr = np.array(list_of_int)
print(arr)

print('**'*20)
arr_range = np.arange(50, 100)
print(arr_range)

print('**'*20)
arr_shape = arr_range.reshape(5,10)
print(arr_shape)
print('**'*20)
#grab 2*2 from the above matrix
print(arr_shape[1:3,1:3])
print('*****Add Array*****')
print(arr_shape + arr_shape)

print('**'*20)
arr_in_between = np.linspace(3,10,4)
print(arr_in_between)

print('**'*20)
zeros = np.zeros((5,5))
print(zeros)

print('**'*20)
ones = np.ones((5,5))
print(ones)

print('**'*20)
one_in_diagonal = np.eye(6, 6)
print(one_in_diagonal)
print('##'*20)
#Slicing
arr_sli = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr_sli)
print('##'*20)
print(arr_sli[:2,1:])