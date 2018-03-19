import numpy as np

#Craete an array of 10 zeros
print(np.zeros(10))

#Create an array of 10 Ones
print(np.ones(10))

#Create an array of 10 Fives
print(np.ones(10) * 5)

#Craete an array of range 10 to 50
print(np.arange(10,51))

#Create an array of all even integers b/w 10 and 50
arr = np.arange(10,51)
print(arr[arr%2==0])
print(np.arange(10,51,2)) #This is also correct solution

#Create a 3*3 matrix b/w 0 and 8
print(np.arange(9).reshape(3,3))

#Create 3*3 Identity matrix
print(np.eye(3))

#Create a random number b/w o and 1
print(np.random.rand(1))

#Create  equally distributed array
print(np.linspace(0.01, 1, 100).reshape(10,10))