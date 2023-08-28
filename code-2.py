# Write the following function, that splits passed arr into two arrays, 
# the first containing values smaller than the value and the second array containing values larger than the value.

arr = [1, 4, 2, 5, 3, 7]

middle_index = len(arr)//2 # middle index of array

arr.sort() # sorted array to asc order

first_array = arr[:middle_index] # first_array values [1,2,3]

second_array = arr[middle_index:] # second_array values [4,5,7]

print(first_array, second_array) # Output [1,2,3] [4,5,7]