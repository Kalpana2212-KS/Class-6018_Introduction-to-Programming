Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Question 2: Given an input list of any level of complexity/nestedness, return the inner most list plus 1. Use recursion method
... #Define function and give argument as input_list
... def find_innermost_list_plus_one(input_list):
...     innermost = None
... # Iterate through the items of input_list
...     for item in input_list:
...         if isinstance(item, list):
... # If the item is a list, reursively call the function
...             innermost = find_innermost_list_plus_one(item)
...     if innermost is None:
...         return [x + 1 for x in input_list]
...     return innermost
... 
>>> 
... # Return results by adding '1' to each element of the innermost list
... input_list = [1, 2, 3, 4, [5, 6, 7, [14, 16]]]
>>> result = find_innermost_list_plus_one(input_list)
>>> # Print the results
... print(result)
[15, 17]
