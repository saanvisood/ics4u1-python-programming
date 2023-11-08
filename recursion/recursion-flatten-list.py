def flatten_list(my_list):

    if my_list == []: #Base case/best case scenario
        return my_list
    
    if type(my_list[0]) == list: #Recurisve case
        return flatten_list(my_list[0]) + flatten_list(my_list[1:])
    
    return my_list[:1] + flatten_list(my_list[1:])

my_list = [1, 2, 3, [[0,7], 9, 8], 5, 6]
print(flatten_list(my_list))