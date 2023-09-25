Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Question 1: Given an input list of any level of complexity/nestedness, return the inner most list plus 1. Use while loop
... # Define function and add arguement as input_list
... def find_innermost_list_plus_one(input_list):
...     while True:
...         inner_list = None
... #Iterate through the input_list
...         for item in input_list:
...             if isinstance(item, list):
...                 inner_list = item
...                 break 
... #Break the loop if inner list identified
...         if inner_list is None:
...             break # If no inner list identified, exit the loop
...         input_list = inner_list
...     return [x + 1 for x in input_list]
... 
>>> #Define input_list and Print result if script is being run in main program
... if __name__ == "__main__":
...     input_list = [1, 2, 3, 4, [5, 6, 7, [10, 12, 15,18]]]
...     result = find_innermost_list_plus_one(input_list)
...     print(result)
... 
...     
[11, 13, 16, 19]
