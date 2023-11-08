def index_list(some_list, item):

    if some_list[0] == item: #Base case
        return 0
    
    else: #Recursive case
        return 1+index_list(some_list[1:], item)
    
some_list = [1, 2, 3, 4]
print(index_list(some_list, 4)) #1
some_list = [8, 9, 5]
print(index_list(some_list, 5)) #2
some_list = [8, 7]
print(index_list(some_list, 7)) #1
some_list = [4]
print(index_list(some_list, 4)) #0