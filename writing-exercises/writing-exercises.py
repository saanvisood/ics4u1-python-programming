# Exercise 1

import random

def fake_people_gen():
    #Person ID in the form of NNN-NN-NNN
    id_1 = random.randint(100, 999)
    id_2 = random.randint(10, 99)
    id_3 = random.randint(1000, 9999)
    s = f'{id_1}-{id_2}-{id_3}'

    return s

print (fake_people_gen())