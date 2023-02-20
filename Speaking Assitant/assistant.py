from helpers.greeting import greeting, ask_for_command, saying, exit_command, not_recognized, say_joke, play_song, \
    forecast

greeting()

while True:
    command = ask_for_command()
    if "name" in command:
        saying()
    elif "joke" in command:
        say_joke()
    elif 'weather' in command:
        forecast()
    elif 'song' in command or 'listen something' in command:
        play_song()
        break
    elif "see you soon" in command or "bye" in command or 'exit' in command:
        exit_command()
        break
    else:
        not_recognized()
