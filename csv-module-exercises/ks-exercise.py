# Exercise 3

import csv

ks_dict = {}

def parse_kickstarter(filename):

    with open (filename, 'r') as file_in:

        header = file_in.readline()

        reader = csv.reader(file_in)

        for line in reader:
            ks_info = [line[9], line[11], line[4], line[1], line[5], line[6], line[8], line[10]]

            if line[2] not in ks_dict:
                ks_info_list = [ks_info]
                ks_dict[line[2]] = ks_info_list
            else:
                ks_info_list.append(ks_info)

        file_in.close()

        return ks_dict


def calc_rate(ks_dict):

    state_list = []

    for key in ks_dict.keys(): #Should refer to ks_info_list since key = category and value = ks_info

        value = ks_dict[key]

        for val in value:

            state_list.append(val[0])

            # if val[0] != 'successful' and val[0] != 'failed' and val[0] != 'canceled':
            #     print(val)
            # Checking if there are any other values other than successful, failed, or canceled

        success_count = state_list.count('successful')
        failed_count = state_list.count('failed')
        canceled_count = state_list.count('canceled')

        print(f'{key} = Success rate: {(success_count/len(state_list))*100:.1f}%, Failed rate: {(failed_count/len(state_list))*100:.1f}%, Cancelled rate: {(canceled_count/len(state_list))*100:.1f}%')
        state_list = []
            
parse_kickstarter("/Users/saanvi/workspace/projects/ics4u1-practice-exercises/csv-module-exercises/ks-data.csv")

calc_rate(ks_dict)