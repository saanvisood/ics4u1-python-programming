# Chapter 6, exercise 2

def day_name(num):
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', \
            'Friday', 'Saturday', 'Sunday']

    if num > 7:
        return None

    print(week[num-1])

day_name(3)
day_name(6)
day_name(42)

# Chapter 6, exercise 6

def days_in_month(month):
    months = ['January', 31, 'February', 28, 'March', 31, 'April', 30, 'May', 31, \
              'June', 30, 'July', 31, 'August', 31, 'September', 30, \
                'October', 31, 'November', 30, 'December', 31]
    

    day_index = months.index(month)+1
    print(months[day_index])

days_in_month("February")
days_in_month("December")

# Chapter 6, exercise 13

def slope(x1, y1, x2, y2):
    m = (y2 - y1)/(x2 - x1)
    return (m)
    # print(f'{m:.1f}')

# slope(5, 3, 4, 2)
# slope(1, 2, 3, 2)
# slope(1, 2, 3, 3)
# slope(2, 4 ,1, 2)

def intercept(x1, y1, x2, y2):
    y_int = y1 - slope(x1, y1, x2, y2)*x1
    print (f'{y_int:.1f}')

intercept(1, 6, 3, 12)
intercept(6, 1, 1, 6)
intercept(4, 6, 12, 8)

# Chapter 6, exercise 16

def is_factor(f, n):
    if n % f == 0:
        return True
    
    return False

print (is_factor(3, 12))
print (not is_factor(5, 12))
print (is_factor(7, 14))
print (not is_factor(7, 15))
print (is_factor(1, 15))
print (is_factor(15, 15))
print (not is_factor(25, 15))

# Chapter 6, exercise 17

def is_multiple(m, n):
    if m % n == 0:
        return True

    return False

print (is_multiple(12, 3))
print (is_multiple(12, 4))
print (not is_multiple(12, 5))
print (is_multiple(12, 6))
print (not is_multiple(12, 7))

# Q1

def right_justify(s, n):
    print (f'{s:>{n}}')

right_justify('Saanvi', 8)

# Q2


# Q3


# Q4