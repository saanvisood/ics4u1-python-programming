# Exercise 1

import csv

def parse_pokemon(filename):
    pokemon_dict = {}
    with open(filename, 'r', encoding = 'utf-8', errors = 'ignore') as file_in:

        header = file_in.readline()

        reader = csv.reader(file_in)

        for line in reader:
            pokemon_info = [line[1], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12]]
            if line[2] not in pokemon_dict:
                pokemon_info_list = [pokemon_info]
                pokemon_dict[line[2]] = pokemon_info_list
            else:
                pokemon_info_list.append(pokemon_info)

    file_in.close()

    return pokemon_dict

def write_pokemon(filename, pokemon_types):
    with open(filename, 'w', encoding = 'utf-8', errors = 'ignore') as file_out:

        for type in pokemon_types.keys():
            pokemon_type = pokemon_types[type]
            file_out.write(f'{type}\n')
            file_out.write(f'{len(pokemon_type)}\n')
            for pokemon in pokemon_type:
                pokemon_info_str = (f'{pokemon[0]},{pokemon[1]},{pokemon[2]},{pokemon[3]},{pokemon[4]},{pokemon[5]},{pokemon[6]},{pokemon[7]},{pokemon[8]},{pokemon[9]},{pokemon[10]}\n')
                file_out.write(pokemon_info_str)

    file_out.close()
    
pokemon_dict = parse_pokemon("/Users/saanvi/workspace/projects/ics4u1-practice-exercises/csv-module-exercises/pokemon-data.csv")
write_pokemon("/Users/saanvi/workspace/projects/ics4u1-practice-exercises/csv-module-exercises/new-pokemon.csv", pokemon_dict)