# Billboard Hot 100 File I/O Project -- ICS4U1
# Saanvi Sood

import csv

def parse_artists(filename):
    song_dict = {}

    with open (filename, 'r') as file_in:
        header = file_in.readline()
        reader = csv.reader(file_in)

        for line in reader:
            id_dict = {}
            artist = line[2]
            song_id = line[0]
            artist_id = line[1]
            ordinal = line[-1]
            
            id_dict['Song_ID'] = song_id
            id_dict['Artist_ID'] = artist_id
            id_dict['Ordinal'] = ordinal

            if song_id not in song_dict:
                song_dict[song_id] = []
            #     artist_dict[artist].append(id_dict)
            # else:
            #     artist_dict[artist].append(id_dict)


    file_in.close()

    return song_dict


def parse_tracks(filename, song_dict):

    with open (filename, 'r') as file_in:

        header = file_in.readline()
        reader = csv.reader(file_in)

        for line in reader:
            song_info_dict = {}

            song_id = line[0]
            artist = line[3]
            song = line[4]
            date = line[2]
            weeks_on_chart = line[6]
            peak_rank = line[-1]

            if song_id in song_dict:

                song_info_dict['Song'] = song
                song_info_dict['Artist'] = artist
                song_info_dict['Date'] = date
                song_info_dict['Weeks_on_Chart'] = weeks_on_chart
                song_info_dict['Peak_Rank'] = peak_rank

                existing_songs_list = song_dict[song_id]
                existing_songs_list.append(song_info_dict)

    file_in.close()

    return song_dict


def main():

    song_dict = parse_artists("/Users/saanvi/Downloads/billboard-hot-100-project/billboard-hot-100-artists.csv")
    parse_tracks("/Users/saanvi/Downloads/billboard-hot-100-project/billboard-hot-100-tracks.csv", song_dict)


main()