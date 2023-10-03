import csv

def create_kerala_districts(filename):
    
    kerala_flood_info = {}
    district_details = {}

    with open(filename, "r") as file_in:

        header = file_in.readline()

        reader = csv.reader(file_in)

        for line in reader:
            
            district = line[0]

            district_details['fatalities'] = int(line[1])
            district_details['num_camps'] = int(line[2])
            district_details['actual_rainfall_mm'] = float(line[3])
            district_details['normal_rainfall_mm'] = float(line[4])
            district_details['no_landslides'] = int(line[5])
            district_details['num_damaged_houses'] = int(line[6])

            kerala_flood_info[district] = district_details

    file_in.close()

    return kerala_flood_info
        


def add_kerala_flood_warnings(filename, kerala_flood_info):

    with open(filename, "r") as file_in:

        warnings_dict = {}  
        header = file_in.readline()
        reader = csv.reader(file_in)

        for line in reader:

            warning_info_list = []
            district = line[0]

            warning_info = [line[1], line[2], line[3]]
            warning_info_list.append(warning_info)

            if district not in warnings_dict:
                warnings_dict[district] = warning_info_list
            else:
                warnings_dict[district].append(warning_info)
            
        for district in kerala_flood_info.keys():
            if district in warnings_dict:
                flood_info = kerala_flood_info[district]
                warnings = warnings_dict[district]
                flood_info['warnings'] = warnings



def print_kerala_flood_info(kerala_flood_info):
    for key in (kerala_flood_info):
        print(key)
        print(kerala_flood_info[key])



def main():
    

      flood_dict = create_kerala_districts("/Users/saanvi/workspace/projects/ics4u1-practice-exercises/matching-keys-exercises/district_wise_details.csv")
      add_kerala_flood_warnings("/Users/saanvi/workspace/projects/ics4u1-practice-exercises/matching-keys-exercises/warnings_actual_predicted.csv", flood_dict)

      print_kerala_flood_info(flood_dict)

main()