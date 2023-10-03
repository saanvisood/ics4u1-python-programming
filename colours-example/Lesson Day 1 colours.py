#create a master holding list for all colours

def generate_colours_list(filename):
    lego_colours = []

    with open(filename) as file_in:

        file_in.readline()

        for line in file_in:

            line = line.strip().split(",")

            #create a list for each colour in file
            #[id, name, hex, transparency]
            temp_entry = []
            temp_entry.append(int(line[0]))
            temp_entry.append(line[1])
            temp_entry.append('#' + line[2])

            #turn 'f' and 't' value of transparency into a boolean
            if line[3] == 'f':
                temp_entry.append(False)
            else:
                temp_entry.append(True)


            lego_colours.append(temp_entry)

    return lego_colours


def print_colours_list(some_list):
    #print the first 10 items of master list
    for colour in some_list:
        print(colour)


colours_list = generate_colours_list('colors.csv')
#print_colours_list(colours_list)
print(colours_list[:5])
