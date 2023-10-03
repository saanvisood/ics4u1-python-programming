import glob
import csv

file_folder = "/Users/saanvi/workspace/projects/ics4u1-practice-exercises/spotify_charts_2022/"

def parse_spotify(all_filenames):

    song_by_artist_dict = {}

    for filename in all_filenames:

        date = filename[22:32]

        with open(file_folder+filename, 'r') as file_in:

            header = file_in.readline() #File header, ignoring it
            reader = csv.reader(file_in)

            for line in reader:
                song_by_artist = f'{line[3]} by {line[2]}'
                if song_by_artist not in song_by_artist_dict:
                    song_by_artist_dict[song_by_artist] = {date:line[-1]}
                else:
                    existing_song_artist = song_by_artist_dict[song_by_artist]
                    existing_song_artist[date] = line[-1]

        file_in.close()


    return song_by_artist_dict


filenames = glob.glob('regional-global-daily-2022-09-*.csv')

print(parse_spotify(filenames))