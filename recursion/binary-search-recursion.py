#Binary search recursion

def binary_search(nums, low, high, num):

    mid = (low+high)//2
    if num == nums[mid]:
        return nums.index(num)
    elif high == low:
        return -1
    elif num < nums[mid]:
        return binary_search(nums, low, mid - 1, num)
    elif num > nums[mid]:
        return binary_search(nums, mid + 1, high, num)

nums = [1, 19, 33, 44, 105, 555, 777, 2918]
print(binary_search(nums, 0, len(nums)-1, 5921))