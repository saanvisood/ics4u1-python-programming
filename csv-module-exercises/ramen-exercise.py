#Exercise 2

import csv

def parse_ramen(filename):

    style_dict = {}
    country_dict = {}

    with open(filename, 'r', encoding = 'utf-8', errors = 'ignore') as file_in:

        header = file_in.readline()

        reader = csv.reader(file_in)

        for line in file_in:
            info_list = line.strip().split(',')

            if len(info_list) == 7:
                style_name = info_list[3]
                country_name = info_list[4]
                noodle_info = [info_list[1], info_list[2], info_list[5]]

                if country_name not in country_dict:
                    noodle_info_list = [noodle_info]
                    style_dict[style_name] = noodle_info_list
                    country_dict[country_name] = style_dict
                else:
                    existing_country_styles = country_dict[country_name] #Dict
                    if style_name not in existing_country_styles:
                        existing_country_styles[style_name] = noodle_info
                    else:
                        existing_country_styles[style_name].append(noodle_info)

    print(country_dict)
    file_in.close()

    return country_dict


parse_ramen("/Users/saanvi/workspace/projects/ics4u1-practice-exercises/csv-module-exercises/ramen-ratings.csv")