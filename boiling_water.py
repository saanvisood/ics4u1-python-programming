def seaLevel():
    temp = int(input('Enter a temperature between 80\u00b0C and 20\u00b0C: '))

    if temp < 80 or temp > 200:
        print (f'{temp} is not within the specified range.')
        seaLevel()

    pressure = 5 * temp - 400
    print (f'{pressure} kPa')
    if pressure < 100:
        print (1)
    elif pressure > 100:
        print (-1)

    print (0)

seaLevel()