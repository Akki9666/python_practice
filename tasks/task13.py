""" 
Even numbers which are divided by 4 and 8 from 1 to 100 
							   using list comprehension
filter the negative numbers using filter
take float inputs separated by '-'
"""


print([i for i  in range(1, 100) if i%4==0 and i%8==0])

arr = [1, 3, -2, 1, -23, -34]
print(list(filter(lambda x:x<0, arr)))

