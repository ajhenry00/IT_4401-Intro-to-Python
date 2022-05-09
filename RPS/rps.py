# Aidan Henry
# This program creates a menu-driven game of rock, paper, scissors
import random


def game_setup(mode):
    stats_list = ["", 0, 0, 0]
    player_name = input("What is your name? ")
    if mode == "new":
        print("Hello " + player_name + ". Let's play!")
        file = open(player_name + ".rps", "w")
        stats_list[0] = player_name
    elif mode == "load":
        print("\nWelcome back " + player_name + ". Let's play!")
        print(stats_list)
        try:
            file = open(player_name + ".rps", "r")
            new_list = []
            for i in range(len(stats_list)):
                new_list.append(file.readline().strip("\n"))
                if i > 0:
                    new_list[i] = int(new_list[i])
            file.close()
            stats_list = new_list
            file = open(player_name + ".rps", "w")
        except FileNotFoundError:
            print(player_name + ", your game could not be found.\n")
            menu()
    stats_list = game(stats_list)
    game_menu(stats_list, file)


def game(stats_list):
    rounds = 0
    for i in range(len(stats_list) - 1):
        rounds += stats_list[i + 1]
    print("\nRound " + str(rounds) + "\n")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    while True:
        try:
            player_choice = int(input("\nWhat will it be? "))
            computer_choice = random.randrange(1, 4)
            if player_choice == computer_choice:
                outcome = 6
                break
            elif player_choice == 1:
                if computer_choice == 3:
                    outcome = 4
                else:
                    outcome = 5
                break
            elif player_choice == 2:
                if computer_choice == 1:
                    outcome = 4
                else:
                    outcome = 5
                break
            elif player_choice == 3:
                if computer_choice == 2:
                    outcome = 4
                else:
                    outcome = 5
                break
            else:
                print("Number out of range. Please choose a number between 1 and 3")
        except ValueError:
            print(" Invalid choice. Please try again")
    player_choice_string = string_construction(player_choice)
    computer_choice_string = string_construction(computer_choice)

    outcome_string = string_construction(outcome)
    print("\nYou chose " + player_choice_string + ". The computer chose " + computer_choice_string +
          ". You " + outcome_string + "!\n")
    if outcome == 4:
        stats_list[1] += 1
    elif outcome == 5:
        stats_list[2] += 1
    else:
        stats_list[3] += 1
    return stats_list


def string_construction(choice):
    string = ""
    if choice == 1:
        string = "Rock"
    elif choice == 2:
        string = "Paper"
    elif choice == 3:
        string = "Scissors"
    elif choice == 4:
        string = "win"
    elif choice == 5:
        string = "lost"
    elif choice == 6:
        string = "tied"
    return string


def game_menu(stats_list, file):
    while True:
        print("What would you like to do?\n")
        print("1. Play Again ")
        print("2. View Statistics")
        print("3. Quit")
        try:
            player_choice = int(input("\nEnter choice: "))
            if player_choice == 1:
                stats_list = game(stats_list)
            elif player_choice == 2:
                view_statistics(stats_list)
            elif player_choice == 3:
                string_list = [stats_list[0], str(stats_list[1]), str(stats_list[2]), str(stats_list[3])]
                for item in string_list:
                    file.write(item + "\n")
                file.close()
                print(stats_list[0] + ", your game has been saved")
                exit()
            else:
                print("Number out of range. Please choose a number between 1 and 3")
        except ValueError:
            print(" Invalid choice. Please try again")


def view_statistics(stats_list):
    name = stats_list[0]
    wins = stats_list[1]
    losses = stats_list[2]
    ties = stats_list[3]
    if losses == 0:
        ratio = "Not enough losses to calculate ratio"
    else:
        ratio = "{:.2f}".format(wins/losses)
    print(name + ", here are your game play statistics...")
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    print("Ties: " + str(ties))
    print("Win/Loss Ratio: " + ratio)


def menu():
    print("Welcome to Rock, Paper, Scissors!\n")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit")
    while True:
        try:
            player_choice = int(input("\nEnter choice: "))
            if player_choice == 1:
                game_setup("new")
            elif player_choice == 2:
                game_setup("load")
            elif player_choice == 3:
                exit()
            else:
                print("Number out of range. Please choose a number between 1 and 3")
        except ValueError:
            print(" Invalid choice. Please try again")


def main():
    menu()


main()
