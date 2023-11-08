def sum_list(a_list):

    if len(a_list) == 1: #Base case/best case scenario
        return a_list[0]
    
    else: #Recursive case
        return a_list[0] + sum_list((a_list[1:]))

list = [1, 2, 3, 4, 5]
print(sum_list(list))