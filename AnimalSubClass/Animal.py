# Aidan Henry
# Animal Class program that defines the Animal class.
# For use when generating Animal Objects.

import random


class Animal:
    def __init__(self, __animal_type, __name):
        self.__animal_type = __animal_type
        self.__name = __name
        mood_number = random.randrange(1, 4)
        if mood_number == 1:
            self.__mood = "happy"
        elif mood_number == 2:
            self.__mood = "hungry"
        else:
            self.__mood = "sleepy"

    def get_animal_type(self):
        return self.__animal_type

    def get_name(self):
        return self.__name

    def get_mood(self):
        return self.__mood


class Mammal(Animal):
    def __init__(self, __animal_type, __name, __hair_color):
        Animal.__init__(self, __animal_type, __name)
        self.__hair_color = __hair_color

    def get_hair_color(self):
        return self.__hair_color


class Bird(Animal):
    def __init__(self, __animal_type, __name, __can_fly):
        Animal.__init__(self, __animal_type, __name)
        self.__can_fly = __can_fly

    def get_can_fly(self):
        return self.__can_fly
