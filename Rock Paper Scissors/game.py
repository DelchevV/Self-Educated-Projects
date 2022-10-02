import random
import colorama

choices = ['R', 'P', 'S']
score = {
    'computer': 0,
    'user': 0
}

# validation for user input for rounds
while True:
    try:
        rounds = int(input(colorama.Fore.WHITE + 'How many rounds you want to play: '))
        if 0 < rounds <= 100:
            points_for_win = rounds // 2 + 1
            break
        else:
            print(colorama.Fore.RED + 'Number must be between 0 and 100')
    except ValueError:
        print(colorama.Fore.RED + "Please enter valid number from 0 to 100")
print()
for current_round in range(rounds):

    # make validation for user input
    while True:
        user_choice = input(colorama.Fore.WHITE + "Make a choice [R/S/P]: ").upper()
        if user_choice in choices:
            break
        else:
            print(colorama.Fore.RED + "Please enter valid command for choice R-for rock, S-for scissors, P-for paper")
            continue

    # computer makes his crandom choice
    computer_choice = random.choice(choices)

    # make conclusion which choice is better and add winning point to his stat
    if user_choice == computer_choice:
        print(colorama.Fore.CYAN + 'Tie!')
    elif user_choice == "R":
        if computer_choice == 'P':
            print(colorama.Fore.YELLOW + f"Opponent wins with {computer_choice}!")
            score['computer'] += 1
        elif computer_choice == 'S':
            print(colorama.Fore.GREEN + f'You win! Opponent chose {computer_choice}')
            score['user'] += 1
    elif user_choice == "P":
        if computer_choice == 'S':
            print(colorama.Fore.YELLOW + f"Opponent wins with {computer_choice}!")
            score['computer'] += 1
        elif computer_choice == 'R':
            print(colorama.Fore.GREEN + f'You win! Opponent chose {computer_choice}')
            score['user'] += 1
    elif user_choice == "S":
        if computer_choice == "R":
            print(colorama.Fore.YELLOW + f"Opponent wins with {computer_choice}!")
            score['computer'] += 1
        elif computer_choice == "P":
            print(colorama.Fore.GREEN + f'You win! Opponent chose {computer_choice}')
            score['user'] += 1

    # if one of the contestants reach rounds/2+1 wins the game
    if score["user"] == points_for_win:
        print()
        print(colorama.Fore.GREEN + f'Winner for this session is User with {score["user"]} points')
        break
    elif score['computer'] == points_for_win:
        print()
        print(colorama.Fore.YELLOW + f'Winner for this session is Computer with {score["computer"]} points')
        break
    elif current_round == rounds - 1:
        if score['computer'] > score['user']:
            print()
            print(colorama.Fore.YELLOW + f'Winner for this session is Computer with {score["computer"]} points')
        elif score['user'] > score['computer']:
            print()
            print(colorama.Fore.GREEN + f'Winner for this session is User with {score["user"]} points')
        else:
            print()
            print(colorama.Fore.RED + 'Match is Tie!')
