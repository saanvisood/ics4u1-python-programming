'''
This method should print the sum of squares from 1 to n
For example sumOfSquares(4) = 30
1^2 + 2^2 + 3^2 + 4^2 = 30
'''
def sumOfSquares(n):
    if n == 0: #Changed n == 1 to n == 0
        return 0
    
    else:
        return (n**2) + sumOfSquares(n - 1) #Error, n+n changed to n**2 and (n + 1) changed to (n - 1)

print (sumOfSquares(4))