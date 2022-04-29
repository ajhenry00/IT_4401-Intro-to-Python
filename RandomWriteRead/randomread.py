#Random Read
# Author: Aidan Henry

def open_file():
    while(True):
        try:
            file_to_read = open("randomnum.txt", "rt")
        except:
            print("File does not exist in this directory.")
            exit()
        else:
            return file_to_read

def get_random_numbers_and_count(file_to_read):
    random_num_amount = 0
    for line in file_to_read:
        random_num_amount += 1
        print(line)
    print("Random number count:", random_num_amount)

def main():
    file_to_read = open_file()
    print("List of random numbers in randomnum.txt: ")
    get_random_numbers_and_count(file_to_read)
    file_to_read.close()
main()
