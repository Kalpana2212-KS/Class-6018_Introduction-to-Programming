Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #HomeWork: NumPy
>>> #Question 1: Import numpy as np and print the version number.
>>> import numpy as np
>>> print(np.__version__)
1.26.0
>>> 
>>> 
>>> #Question 2: Create a 1D array of numbers from 0 to 9.
>>> array = np.arange(10)
>>> print("Array:", array)
Array: [0 1 2 3 4 5 6 7 8 9]
>>> 
>>> 
>>> #Question 3: Import a dataset with numbers and texts keeping the text intact in python numpy.
>>> #First, downloaded the iris data set to local windows.
>>> file_path = "C:\\Users\\Student\\Desktop\\HW_NumPy\\iris.data.txt"
>>> # delimiter= splits values at each coma
>>> #dtype set to 'None'.Since the file contains both text & numbers,NumPy automatically determines appropriate datatype
>>> # encoding = utf-8.Ensures text file is read and represented correctly.
>>> data = np.genfromtxt(file_path, delimiter = ',', dtype = None, encoding = 'utf-8')
>>> 
>>> # Check if the data is imported accurately.
>>> print(data[:5])
[(5.1, 3.5, 1.4, 0.2, 'Iris-setosa') (4.9, 3. , 1.4, 0.2, 'Iris-setosa')
 (4.7, 3.2, 1.3, 0.2, 'Iris-setosa') (4.6, 3.1, 1.5, 0.2, 'Iris-setosa')
 (5. , 3.6, 1.4, 0.2, 'Iris-setosa')]
>>> 
>>> 
>>> # Question 4: Find the position of the 1st occurrence of a value > 1.0 in petalwidth 4th column of iris dataset
>>> data = np.genfromtxt(file_path, delimiter = ',', dtype = float, encoding = 'utf-8', usecols = (0,1,2,3))
# dtype is floats only. Using columns 0 to 3 (i,e first 4 columns)
petal_width = data[:,3]
# Extract 4th column: petal width
position = np.argmax(petal_width > 1.0)
# Find the position of the first occurrence of a value > 1.0.
print("The position of the first occurrence of a value greater than 1.0 in petal width is:", position)
The position of the first occurrence of a value greater than 1.0 in petal width is: 50


#Question 5:From the array a, replace all values greater than 30 to 30 and less than 10 to 10.
np.random.seed(100)
a = np.random.uniform(1,50,20)
print(a)
[27.62684215 14.64009987 21.80136195 42.39403048  1.23122395  6.95688692
 33.86670515 41.466785    7.69862289 29.17957314 44.67477576 11.25090398
 10.08108276  6.31046763 11.76517714 48.95256545 40.77247431  9.42510962
 40.99501269 14.42961361]


# Replace values greater than 30 with 30
a[a > 30] = 30
print(a)
[27.62684215 14.64009987 21.80136195 30.          1.23122395  6.95688692
 30.         30.          7.69862289 29.17957314 30.         11.25090398
 10.08108276  6.31046763 11.76517714 30.         30.          9.42510962
 30.         14.42961361]


# Replace values less than 10 with 10
a[a < 10] = 10
print(a)
[27.62684215 14.64009987 21.80136195 30.         10.         10.
 30.         30.         10.         29.17957314 30.         11.25090398
 10.08108276 10.         11.76517714 30.         30.         10.
 30.         14.42961361]
