import random


def pick_joke():
    jokes = [
        'Hear about the new restaurant called Karma?    '
        'There’s no menu: You get what you deserve.',
        'Did you hear about the claustrophobic astronaut?      '
        'He just needed a little space.',
        'Why did the teddy bear skip out on dessert when she was on a date?      '
        'She was stuffed!',
        'What do you call a noodle that is fake?      '
        'An im-pasta.',
        'What’s an alligator in a vest called?       '
        'An investi-gator'
    ]

    joke = random.choice(jokes)
    return joke
