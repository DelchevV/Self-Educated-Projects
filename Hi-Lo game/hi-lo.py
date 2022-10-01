import random
import colorama


def play_again(states, live):
    # if you win level diff rise by 1 else stay same

    if states == "win":
        number = random.randint(1, 10 * (level + 1))
        live += 3
        return number, live
    elif states == 'lose':
        live = 3
        number = random.randint(1, 10 * level)
        return number, live


score = {'losses': 0,
         'wins': 0}

while True:
    try:
        level = int(input(colorama.Fore.WHITE + 'Enter difficulty level 1 to 10: '))
        if level <= 0:
            print(colorama.Fore.RED + "Invalid Number!")
            continue
        else:
            break
    except ValueError:
        print(colorama.Fore.RED + "Please enter a valid number greater than 0")

guessing_number = random.randint(1, 10 * level)
lives = 3

while True:
    # check for lives > 0
    if lives == 0:
        print(colorama.Fore.RED + 'You lost! :(')
        state = 'lose'
        score['losses'] += 1
        ask = input(colorama.Fore.RED + 'Wanna try again? :)[y/n]: ')
        if ask=="y":
            guessing_number, lives = play_again(state, lives)
            continue
        else:
            break

    # user make a guess
    user_num = int(input(colorama.Fore.WHITE + "Enter a guess: "))
    lives -= 1
    if user_num == guessing_number:
        print(colorama.Fore.GREEN + "You guessed it! Congrats!")
        state = 'win'
        score['wins'] += 1
        ask = input(colorama.Fore.GREEN + 'Do you want to play again [y/n]: ')
        if ask == 'y':
            guessing_number, lives = play_again(state, lives)
            print(
                colorama.Fore.YELLOW + f'Your level difficulty is raised by 1 and you got 3 more lives, total {lives} lives')
            continue
        else:
            break

    # computer say higher or lower depending on user guess
    elif user_num < guessing_number:
        print(colorama.Fore.YELLOW + 'Higher')
    elif user_num > guessing_number:
        print(colorama.Fore.YELLOW + 'Lower')

# print scoreboard
print(colorama.Fore.YELLOW + f'Here is your score of the last game session:')
for key, value in score.items():
    print(colorama.Fore.YELLOW + f'{key}: {value}')
print()
print(colorama.Fore.WHITE + 'Glad you played! Hope see you again!')
