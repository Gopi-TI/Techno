# Write a function to remove duplicates from a sorted array. Use any language of your choice.

# python code

# here i used set function it removes the duplicates from set and gives unique set
sorted_Array = [1, 1, 1, 2, 2, 3, 4, 5, 5]
    
# after that i converted set type into list type
unique_array = list(set(sorted_Array))

print(unique_array)

# Output [1,2,3,4,5]