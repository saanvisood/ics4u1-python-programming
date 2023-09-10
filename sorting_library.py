def printNums(inputNums):
        print(inputNums)

def takeInputNumbers():
    nums = []
    numOfNums = int(input("Enter the number of numbers to be sorted: "))
    for i in range(numOfNums):
        user_nums = int(input(f'Enter number {i+1}: '))
        nums.append(user_nums)
    return nums

def selection_sort(inputNums):
    for j in range(0, len(inputNums)):
        for k in range(j, len(inputNums)):
            if inputNums[j] > inputNums[k]:
                temp = inputNums[j]
                inputNums[j] = inputNums[k]
                inputNums[k] = temp

def bubble_sort(inputNums):
    for j in range(0, len(inputNums)):
        for k in range(j, len(inputNums)):
            if inputNums[j] > inputNums[k]:
                temp = inputNums[j]
                inputNums[j] = inputNums[k]
                inputNums[k] = temp

inNum = takeInputNumbers()
printNums(inNum)
selection_sort(inNum)
printNums(inNum)