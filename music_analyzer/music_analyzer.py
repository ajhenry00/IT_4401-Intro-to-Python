# Aidan Henry
# this program analyzes a given playlist data file and outputs summarized results

def load_and_parse(file):
    column_titles = file.readline()
    title_list = column_titles.split("\t")
    title_list[-1] = title_list[-1].strip("\n")
    # print(title_list)
    song_dict = dict()
    for i in range(len(title_list)):
        song_dict.update({title_list[i]: []})
    for line in file:
        song_list = line.split("\t")
        song_list[-1] = song_list[-1].strip("\n")
        # print(song_list)
        key_index = 0
        for key in song_dict.keys():
            song_dict[key].append(song_list[key_index])
            key_index += 1
            if key_index > len(song_list) - 1:
                break
            # print(song_dict[key])
    # print(song_dict["Name"])
    return song_dict


def calculate_total_songs(song_dict):
    return len(song_dict["Name"])


def songs_released_each_given(song_dict, delimiter):
    year_list = song_dict[delimiter]
    unique_year = sorted(set(year_list))
    year_dict = {}
    for year in unique_year:
        year_dict.update({year: year_list.count(year)})
    return year_dict


def calculate_song_time(song_dict, mode):
    time_list = song_dict["Time"]
    new_time = int(time_list[0])
    time_index_list = []
    time_index = 0
    song_time_string = []
    int_time = 0
    if mode == "l":
        for time in time_list:
            if time == '':
                continue
            if int(time) > new_time:
                new_time = int(time)
        for time in time_list:
            if time == '':
                time_index += 1
                continue
            if int(time) == new_time:
                time_index_list.append(time_index)
            time_index += 1
        # print(time_index_list)
    else:
        for time in time_list:
            if time == '':
                continue
            if int(time) < new_time:
                new_time = int(time)
        for time in time_list:
            if time == '':
                time_index += 1
                continue
            if int(time) == new_time:
                time_index_list.append(time_index)
            time_index += 1
    for index in time_index_list:
        song_time_string.append(song_dict["Name"][index] + " by " +
                                song_dict["Artist"][index] + "; length: " + str(new_time))

    return song_time_string


def get_genre_songs(song_dict):
    genre_dict = songs_released_each_given(song_dict, "Genre")
    genre_list = song_dict["Genre"]
    genre_set = set(genre_list)
    longest_dict = {}
    shortest_dict = {}
    for genre in genre_set:
        genre_time_dict = {"Name": [], "Artist": [], 'Time': []}
        genre_index = 0
        genre_index_list = []
        for item in genre_list:
            if item == genre:
                genre_index_list.append(genre_index)
            genre_index += 1
        for index in genre_index_list:
            for key in genre_time_dict.keys():
                genre_time_dict[key].append(song_dict[key][index])
        # print(genre_time_dict)
        longest_dict.update({genre: calculate_song_time(genre_time_dict, "l")})
        shortest_dict.update({genre: calculate_song_time(genre_time_dict, "s")})
    # print(longest_list)
    for pair in genre_dict:
        print(pair + ": " + str(genre_dict[pair]) + " Longest: " + str(longest_dict[pair])
              + " Shortest: " + str(shortest_dict[pair]))
        # print(longest_dict)


def get_songs_played(song_dict):
    played_dict = song_dict["Plays"]
    songs_played = 0
    for value in played_dict:
        if value != '' and int(value) > 0:
            songs_played += 1
    return songs_played


def get_songs_not_played(song_dict):
    total_songs = calculate_total_songs(song_dict)
    songs_played = get_songs_played(song_dict)
    songs_not_played = total_songs - songs_played
    return songs_not_played


def main():
    while True:
        user_file = input("Please enter a data file to analyze: ")
        data_file = open(user_file, "r", encoding="utf-16")
        song_dict = load_and_parse(data_file)
        data_file.close()
        print("Total Songs in Playlist: ")
        print(calculate_total_songs(song_dict))
        year_dict = songs_released_each_given(song_dict, "Year")
        print("\nSongs Released by Year: ")
        for pair in year_dict:
            print(pair + ": " + str(year_dict[pair]))
        print("\nLongest Song: ")
        longest_song_list = calculate_song_time(song_dict, "l")
        for song in longest_song_list:
            print(song)
        print("\nShortest Song: ")
        shortest_song_list = calculate_song_time(song_dict, "s")
        for song in shortest_song_list:
            print(song)
        print("\nData by Genre(# of songs, longest song, shortest song): ")
        get_genre_songs(song_dict)
        print("\nSongs Played: " + str(get_songs_played(song_dict)))
        print("\nSongs Not Played: " + str(get_songs_not_played(song_dict)))
        another_file = input("\nWould you like to analyze another file? ")
        if another_file != 'y':
            break


main()
