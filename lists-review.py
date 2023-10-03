# Q4

def is_sorted(list):
    count = 0
    for i in range(0, len(list)-1):
        if list[i] < list[i+1]:
            count += 1
        else:
            return False
        
    if count == len(list)-1:
        return True

print (is_sorted([1, 2, 3, 4, 8]))
print (is_sorted([3, 1, 2, 10, 11]))

# Q5

def has_duplicates(list):
    for num in list:
        if list.count(num) > 1:
            return True

    return False

print (has_duplicates([1, 1, 2, 5, 6, 7]))
print (has_duplicates([1, 2, 3, 4, 5]))

# Q6

import random

def add_random():
    nums = []
    for i in range(10):
        nums.append(0)

    for i in range(1000):
        randint = random.randint(0, 9)
        nums[randint] = nums[randint]+1

    print (nums)

add_random()