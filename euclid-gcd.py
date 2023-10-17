# Euclid's Algorithm for Finding the Greatest Common Divisor
# Recursive Algorithm*

def main(x, y): #Width and height of rectangle/numbers we want to find GCD of as parameters
    if x > y:
        new_x = x%y
        if new_x > 0:
            return main(new_x, y)
        else:
            return y
    elif x == y:
        return x
    else:
        new_y = y%x
        if new_y > 0:
            return main(x, new_y)
        else:
            return x

print(main(150, 345))