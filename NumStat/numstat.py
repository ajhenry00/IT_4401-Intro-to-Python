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
    return number_list

def get_average(sum, len):
    average = sum / len
    return average

def main():
    do_file_evaluation = True
    while(do_file_evaluation):
        user_file = open_file()
        number_list = get_numbers(user_file)
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
        file_evaluate = input("Would you like to evaluate another file? (y/n):")
        if(file_evaluate != "y"):
            do_file_evaluation = False

main()
