# Q1

import random

def random_nums():
    dict = {}
    for i in range(1, 11):
        dict[i] = 0

    for i in range(1000):
        randint = random.randint(1, 10)
        dict[randint] = dict[randint]+1

    return dict


def calc_frequency(dict):
    print ('Random number frequency')
    for i in range(1, 11):
        pct = f'{dict[i]/10}%'
        print (f'num {i:>2}, chosen {pct:>5} time')

calc_frequency(random_nums())

# Q2

month_dict = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
    
def date_decoder(date):
    date = date.split("-")
    day = date[0]
    month = date[1]
    year = date[2]

    month = month_dict[month]

    if int(year) > 23:
        year = '19'+year
    elif int(year) < 23:
        year = '20'+year

    date_tuple = (day, str(month), year)
    return date_tuple

print (date_decoder('8-MAR-85'))

# Q6

def roll_dice():
    dict = {}
    for i in range(1, 7):
        for j in range(1, 7):
            new_tuple = (i, j)
            sum = i + j
            dict[sum] = new_tuple
    return dict