'''
Day 2 - File IO Lesson
Grouping lines of file
Weather climate data

'''
def isfloat(value):
    value = value.replace(".", "", 1)
    value = value.replace("-", "", 1)

    return value.isdigit()


def create_station_data(filename):

    with open(filename, "r") as fileIn:

        #read and ignore first 32 lines of file
        for i in range(0, 32):
            fileIn.readline()


        station_dictionary = {}
        
        #iterate through file
        for line in fileIn:
            
            line = line.strip().replace('"', "")
            stnData = line.split(",")
            

            #station_name : [values, values, values, values ]
            #Don't forget to change number values to ints or floats as necessary

            data = []

            for item in stnData[1:]:
                if item.isdigit():
                    data.append(int(item))
                elif isfloat(item):
                    data.append(float(item))
                else:
                    data.append(item)

            station_dictionary[stnData[0]] = data

    return station_dictionary
        

def print_stations(station_dictionary):
    for key in station_dict:
        print(f'\n{key}')
        print(station_dict[key])


        

#MAIN
#Goal - generate a dictionary of all stations with their associated data

station_dict = create_station_data("/Users/saanvi/workspace/projects/ics4u1-practice-exercises/grouping-exercises/climate-data.csv")
print_stations(station_dict)