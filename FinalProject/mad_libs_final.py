# Aidan Henry
# Final Project Mad Libs Generator
import string


def load_stories(file):
    file_string = file.read()
    # print(file_string)
    story_list = file_string.split("\n\n")
    return story_list


def parse_stories(story):
    noun_set = set()
    name_set = set()
    place_set = set()
    body_part_set = set()
    building_set = set()
    verb_set = set()
    adjective_set = set()
    clothes_set = set()
    object_set = set()
    food_set = set()
    emotion_set = set()
    town_name_set = set()

    story = story.translate(str.maketrans("", "", string.punctuation))
    word_list = story.split()
    for word in word_list:
        word = word.strip(".")
    for word in word_list:
        if "Noun" in word:
            noun_set.add(word)
        elif "Name" in word:
            if "s" in word:
                continue
            name_set.add(word)
        elif "Place" in word:
            place_set.add(word)
        elif "BodyPart" in word:
            body_part_set.add(word)
        elif "Building" in word:
            building_set.add(word)
        elif "Verb" in word:
            verb_set.add(word)
        elif "Adjective" in word:
            adjective_set.add(word)
        elif "Clothes" in word:
            clothes_set.add(word)
        elif "Object" in word:
            object_set.add(word)
        elif "Food" in word:
            food_set.add(word)
        elif "Emotion" in word:
            emotion_set.add(word)
        elif "Town" in word:
            if "name" in word:
                town_name_set.add(word)
    user_words = sorted(
        set.union(noun_set, name_set, place_set, body_part_set, building_set, verb_set, adjective_set, clothes_set,
                  object_set, food_set, emotion_set, town_name_set))
    print(user_words)
    return user_words


def get_input(user_words):
    mad_libs_dict = dict()
    user_input = []
    for i in range(len(user_words)):
        mad_libs_dict.update({user_words[i]: ""})
    for word in user_words:
        user_input.append(input("Please enter a(n) " + word.lower() + ": "))
    for i in range(len(user_words)):
        mad_libs_dict.update({user_words[i]: user_input[i]})
    return mad_libs_dict


def main():
    story_file = open("madlib_stories.txt", "r")
    stories = []
    stories = load_stories(story_file)
    story_file.close()
    while True:
        try:
            story_choice = input("Would you like Story 1 or 2? Type anything else to quit: ")
            if story_choice == "1" or story_choice == "2":
                story = stories[int(story_choice) - 1]
                user_words = parse_stories(story)
                mad_libs_dict = get_input(user_words)
                # print(mad_libs_dict)
                for key in mad_libs_dict:
                    story = story.replace(key, mad_libs_dict[key])
                print(story)
            else:
                break
        except ValueError:
            print("Invalid choice. Please try again")


main()
