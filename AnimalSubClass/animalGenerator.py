# Aidan Henry
# Generates Animal Objects
# Prints all animals created in appropriate format

import Animal


def main():
    generate_animals = True
    animal_list = []
    print("Welcome to the animal generator!")
    print("This Program creates Animal objects")

    while generate_animals:
        print("\nWould you like to create a mammal or bird?")
        print("1. Mammal")
        print("2. Bird")
        animal_subclass_input = int(input("Which would you like to create? "))
        if animal_subclass_input == 1:
            animal_string = "mammal"
            animal_attributes = get_animal_attributes(animal_string)
            hair_input = input("What color is the " + animal_string + "'s hair? ")
            user_animal = Animal.Mammal(animal_attributes[0], animal_attributes[1], hair_input)
        else:
            animal_string = "bird"
            animal_attributes = get_animal_attributes(animal_string)
            fly_input = input("Can the " + animal_string + " fly? ")
            user_animal = Animal.Bird(animal_attributes[0], animal_attributes[1], fly_input)

        animal_list.append(user_animal)
        check_generate = input("\nWould you like to add more animals (y/n)? ")
        if check_generate != "y":
            generate_animals = False
    print("Animal List:")
    for animal in animal_list:
        print(animal.get_name() + " the " + animal.get_animal_type() + " is " + animal.get_mood())


def get_animal_attributes(animal_string):
    type_input = input("\nWhat type of " + animal_string + " would you like to create? ")
    name_input = input("What is the " + animal_string + "'s name? ")
    animal_attribute_list = [type_input, name_input]
    return animal_attribute_list


main()
