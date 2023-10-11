# Billboard Hot 100 File I/O Project -- ICS4U1
# Saanvi Sood

import csv

folder_path = "/Users/saanvi/workspace/projects/ics4u1-practice-exercises/billboard-hot-100-project/"

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
            id_dict['Artist'] = artist

            if song_id not in song_dict:
                song_dict[song_id] = {}
                song_dict[song_id] = id_dict

    file_in.close()

    return song_dict


def parse_tracks(filename, song_dict):
    artist_song_dict = {}

    with open (filename, 'r') as file_in:
        header = file_in.readline()
        reader = csv.reader(file_in)

        for line in reader:
            song_info_dict = {}
            song_id = line[0]
            artist = line[3]
            song = line[4]
            date = line[2]
            rank = line[1]
            weeks_on_chart = line[6]
            peak_rank = line[-1]

            if song_id not in artist_song_dict:
                artist_song_dict[song_id] = []
                
            song_info_dict['Song'] = song
            song_info_dict['Additional_Artists'] = artist
            song_info_dict['Date'] = date
            song_info_dict['Current_Rank'] = int(rank)
            song_info_dict['Weeks_on_Chart'] = int(weeks_on_chart)
            song_info_dict['Peak_Rank'] = int(peak_rank)

            if song_id in song_dict:
                existing_artist = song_dict[song_id]
                song_info_dict['Artist_ID'] = existing_artist['Artist_ID']
                song_info_dict['Artist'] = existing_artist['Artist']

            existing_songs_list = artist_song_dict[song_id]
            existing_songs_list.append(song_info_dict)

    file_in.close()

    return artist_song_dict


def write_to_file(filename, song_dict):
    artist_dict = {}

    with open (filename, 'w') as file_out:
        header = (f'song_id,artist_id,artist,song,date,current_rank,weeks_on_chart,peak_rank,additional_artists\n')
        file_out.write(header) #Ensuring the CSV file has a header

        for song in song_dict:
            song_charts = song_dict[song]
            for song_chart in song_charts:
                additional_artists = "" #Some songs do not have a feautured, or more than one artist. In that case, leave this field blank
                if song_chart['Artist'] != song_chart['Additional_Artists']:
                    additional_artists = song_chart['Additional_Artists']
                file_out.write(f'{song},{song_chart["Artist_ID"]},{song_chart["Artist"]},{song_chart["Song"]},{song_chart["Date"]},{song_chart["Current_Rank"]},{song_chart["Weeks_on_Chart"]},{song_chart["Peak_Rank"]},{additional_artists}\n')

    file_out.close()


def main():

    song_dict = parse_artists(folder_path+"billboard-hot-100-artists.csv")
    song_info_dict = parse_tracks(folder_path+"billboard-hot-100-tracks.csv", song_dict)
    write_to_file(folder_path+"new-billboard-data.csv", song_info_dict) #Writing to a CSV so it is easy to use again


main()