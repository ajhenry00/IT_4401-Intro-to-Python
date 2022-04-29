# Random Write
# Author: Aidan Henry
import random

def get_valid_num_input(prompt):
    while(True):
        try:
            valid_input = int(input(prompt))
            if(valid_input <= 0):
                print("Value must be positive.")
                continue
        except ValueError:
            print("Only integer values are valid.")
            continue
        else:
            return valid_input

def main():
    input_prompts = ["Please enter quantity of random numbers to generate: ",
                    "Please enter upper bound of numbers: ",
                    "Please enter lower bound of numbers: "]

    for prompt in input_prompts:
        if(prompt == "Please enter quantity of random numbers to generate: "):
            random_num_amount = get_valid_num_input(prompt)
        elif(prompt == "Please enter upper bound of numbers: "):
            upper_bound = get_valid_num_input(prompt)
        else:
            lower_bound = get_valid_num_input(prompt)
    write_file = open("randomnum.txt", "wt")
    for number in range(random_num_amount):
        random_num = random.randint(lower_bound, upper_bound)
        write_file.write(str(random_num) + "\n")
    write_file.close()

main()
