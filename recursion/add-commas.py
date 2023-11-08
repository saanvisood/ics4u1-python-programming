def add_commas(int_str):

    if len(int_str) == 1 or len(int_str) == 2: #Base case/best case scenario
        return int_str
    
    else: #Recursive case, add commas every 3 consecutive integers
        return add_commas(int_str[:-3]) + f',{int_str[-3:]}'
    
int_str = '1234567'
print(add_commas(int_str))