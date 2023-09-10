#Question 1: Sort 4 numbers

w = 8
x = -6
y = 7
z = 5
temp = 0

print (w, x, y, z)

while w > x or w > y or w > z or x > y or x > z or y > z:

    if w > z:
        temp = w
        w = z
        z = temp
    if w > y:
        temp = w
        w = y
        y = temp
    if w > x:
        temp = w
        w = x
        x = temp

    if x > y:
        temp = x
        x = y
        y = temp
    if x > z:
        temp = x
        x = z
        z = temp

    if y > z:
        temp = y
        y = z
        z = temp

        print(w, x, y, z)


#Question 2

def powerOf2(num):
    p = 0
    c = 2

    while c < num:
        p += 1
        c = c*2
    print (f'2^{p} == {2**p} ')

powerOf2(172319)


#Question 3

def calculateWindChill():
    
    print("Calm", end='\t')
    for temp in range(40, -46, -5):
        print(temp, end="\t")
    print("\n")

    for windSpeed in range(5, 41, 5):
        print(f'{windSpeed}', end="\t")
        for temp in range(40, -46, -5):
            windChill = 35.74 + 0.6215*temp - 35.75*(windSpeed**0.16) + 0.4275*temp*(windSpeed**0.16)
            print(f'{windChill:.0f}', end="\t")
        print("\n")

calculateWindChill()


#Question 4

def hailstoneNumbers():

    for num in range(1, 31):
        calculateHailstones(num)
        print("-.-.-.-.-.-.-.-.-.-")


def calculateHailstones(n):

    print(f'Number: {n}\n')
    steps = 0
    hailstones = [n]

    while n != 1 and max(hailstones) != 1:

        if n % 2 == 0:
            n = n/2
            hailstones.append(n)
            steps += 1

        elif n % 2 == 1:
            n = n*3 + 1
            hailstones.append(n)
            steps += 1

    print(f'Number of steps: {steps}')
    maxHailstone = max(hailstones)
    print(f'Maximum value in path: {maxHailstone:.0f}')

hailstoneNumbers()