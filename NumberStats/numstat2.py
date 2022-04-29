# Number Stats
# Author: Aidan Henry

def open_file():
    while(True):
        try:
            user_file_input = input("Please enter name of file: ")
            if(".txt" not in user_file_input):
                print("Invalid file extension.")
                continue
            user_file = open(user_file_input, "rt")
        except:
            print("File not in directory or unable to be read.")
            exit()
        else:
            return user_file

def get_numbers(user_file):
    number_list = []
    for line in user_file:
        number_list.append(int(line))
    number_list.sort()
    return number_list

def get_average(sum, len):
    average = sum / len
    return average

def get_median(number_list):
    median = 0;
    if(len(number_list) == 1):
        median = number_list[0]
    elif(len(number_list) % 2 == 0):
        left_middle = int((len(number_list) / 2) - 1)
        right_middle = left_middle + 1
        median = (number_list[left_middle] + number_list[right_middle]) / 2
    else:
        median_position = int(((len(number_list) + 1) / 2) - 1)
        median = number_list[median_position]
    return median

def get_mode(number_list):
    number_counts = {}
    mode = []
    max_count = 0
    for number in number_list:
        if (number in number_counts):
            number_counts[number] += 1
        else:
            number_counts[number] = 1
        count = number_counts[number]
        if (count > max_count):
            max_count = number_counts[number]
    for number in number_counts:
        if(number_counts[number] == max_count):
            mode.append(number)
    #print(max_count)
    return mode

def main():
    do_file_evaluation = True
    while(do_file_evaluation):
        user_file = open_file()
        number_list = get_numbers(user_file)
        if(number_list == []):
            print("No numbers were found in the file.")
            exit()
        num_sum = sum(number_list)
        num_len = len(number_list)
        max_num = max(number_list)
        min_num = min(number_list)
        range = max_num - min_num
        print("File name:", user_file.name)
        print("Sum:", num_sum)
        print("Count:", num_len)
        print("Average:", get_average(num_sum, num_len))
        print("Maximum:", max_num)
        print("Minimum:", min_num)
        print("Ramge:", range)
        print("Median:", get_median(number_list))
        print("Mode:", get_mode(number_list))
        file_evaluate = input("Would you like to evaluate another file? (y/n):")
        if(file_evaluate != "y"):
            do_file_evaluation = False

main()
