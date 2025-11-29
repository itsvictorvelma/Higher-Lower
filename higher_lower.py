import random
from game_data import data  # our dataset with names, followers, etc.
import os  # for clearing the screen
import art  # ascii art for logo and compare symbol

# clear the terminal screen depending on OS
def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        term = os.environ.get('TERM')
        if term:
            os.system('clear')  # Unix/Linux
        else:
            print("\n" * 100)  # fallback if TERM not set

# return the "person" with more followers
def check_winner(a, b):
    return a if a["follower_count"] > b["follower_count"] else b

# return the "person" with fewer followers
def check_loser(a, b):
    return a if a["follower_count"] < b["follower_count"] else b

def main():
    player_points = 0  # keep track of score

    # pick initial two random options
    option_1, option_2 = random.sample(data, 2)

    while True:
        # figure out who wins and who loses this round
        winner = check_winner(option_1, option_2)
        loser = check_loser(option_1, option_2)

        print(art.logo)

        print(f"\nWho has more followers? || Current Score: {player_points}")

        # show the two options to the player
        print(f"\n1. {option_1['name']} || {option_1['description']}\n")
        print(art.compare)
        print(f"\n2. {option_2['name']} || {option_2['description']}")

        # ask the player for a choice until they give a valid input
        while True:
            choice = input("\n1 or 2?: ")

            if choice == '1':
                selected = option_1
                break

            elif choice == '2':
                selected = option_2
                break

            else:
                print("\nwomp womp, that's not a valid choice try again.")

        # check if player got it right
        if selected == winner:
            player_points = player_points + 1
            # keep the winner for next round, pick new challenger
            option_1 = winner
            option_2 = random.choice([x for x in data if x != option_1])
            print(f"\nCorrect!!")
            print("\nPress 'Enter' To Continue\n")
            input()
            clear_screen()
            continue

        else:
            # player lost, show final results
            clear_screen()
            print(f"\nWrong!! You lose...")
            print(f"\nThe correct answer was: {winner['name']}, with {winner['follower_count']} followers.\n")
            print(f"{loser['name']} only has {loser['follower_count']} followers")
            print(f"\nFinal Score: {player_points}\n")
            return  # exit game

# game loop to allow multiple plays
game_over = False

while not game_over:
    input1 = input("\nWould you like to play a game of 'Higher or Lower'? (y/n): ").lower().strip()

    if input1 == "y":
        clear_screen()
        main()  # start a new game

    if input1 == "n":
        print("\nThank you, come again!")
        game_over = True  # exit loop
