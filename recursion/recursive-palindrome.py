def palindrome(str):

    if len(str) == 1: #Base case/best case scenario
        return str
    
    else: #Recursive case
        return str[-1] + palindrome(str[:-1])
    
str = 'hello world'
print(palindrome(str))