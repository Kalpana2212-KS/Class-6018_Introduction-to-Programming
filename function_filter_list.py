Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Question 3: Using standard function, write a program that, given an input list, will filter the input above a user defined threshold. 
... 
... # Import the reduce function from function tools
... from functools import reduce
>>> #Define function that takes 3 arguements: acc= accumulator list, x = element from input list, threshold value for filtering
... def filter_above_threshold(acc,x,threshold):
...     if x <= threshold:
... # If 'x' is less/equal to threshold, append it to 'acc' list
...         acc.append(x)
... # Return the updated accumulator list
...     return acc
... 
>>> #Define an input_list of integers
... input_list = [1,2,3,4,5,6,7,8,9]
>>> 
>>> # User prompt to enter value, and convert it to integer
... threshold = int(input("Enter the threshold: "))
Enter the threshold: 6
>>> #Use reduce function to apply the 'filter_above_threshold' function. 
... #To each element in the input list and accumulate results in an empty list
... filtered_list = reduce(lambda acc, x: filter_above_threshold(acc, x, threshold), input_list, [])
>>> #Print the filtered list
... print(filtered_list)
[1, 2, 3, 4, 5, 6]
