reverse_dict = {
    'a': 'xooooo',
    'b': 'xoxooo',
    'c': 'xxoooo',
    'd': 'xxoxoo',
    'e': 'xooxoo',
    'f': 'xxxooo',
    'g': 'xxxxoo',
    'h': 'xoxxoo',
    'i': 'oxxooo',
    'j': 'oxxxoo',
    'k': 'xoooxo',
    'l': 'xoxoxo',
    'm': 'xxooxo',
    'n': 'xxoxxo',
    'o': 'xooxxo',
    'p': 'xxxoxo',
    'q': 'xxxxxo',
    'r': 'xoxxxo',
    's': 'oxxoxo',
    't': 'oxxxxo',
    'u': 'xoooxx',
    'v': 'xoxoxx',
    'w': 'oxxxox',
    'x': 'xxooxx',
    'y': 'xxoxxx',
    'z': 'xooxxx',
    ' ': 'oooooo'}

def reverse(reverse_dict):
    braille_dict = {}

    for key in reverse_dict.keys():
        braille_dict[reverse_dict[key]] = key

    return braille_dict
    

def parse_braille_file(filename):

    braille_data = {}
    some_braille = []

    with open(filename) as file_in:

        line_counter = 0
        for line in file_in:
            line_counter += 1
            count = 0
            for i in range(0, len(line)-1, 2):
                if count in braille_data:
                    braille_data[count] += line[i]+line[i+1]
                    count += 1
                else:
                    braille_data[count] = line[i]+line[i+1]
                    count += 1
            
            if line_counter == 3:
                for value in braille_data.values():
                    some_braille.append(value)
                line_counter = 0
                braille_data = {}

    return some_braille


def decode_braille(some_braille, braille_dict):
    print(braille_dict)
    for i in some_braille:
        print(braille_dict[i])

some_braille = parse_braille_file("/Users/saanvi/workspace/projects/ics4u1-practice-exercises/grouping-exercises/braille-data.txt")
braille_dict = reverse(reverse_dict)

decode_braille(some_braille, braille_dict)