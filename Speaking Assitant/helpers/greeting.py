import pyttsx3
import speech_recognition as sr
import webbrowser

from helpers.jokes import pick_joke
from helpers.music import pick_song
from helpers.wheather_scrapper import make_prediction

engine = pyttsx3.init()
engine.setProperty('rate', 190)


def greeting():
    engine.say("Hello! It's you're virtual assistant Natasha")
    engine.runAndWait()


def not_recognized():
    engine.say("Could not recognize your voice!")
    engine.runAndWait()


def ask_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            try:
                engine.say("What you want me to do? ")
                engine.runAndWait()
                audio = r.listen(source, timeout=4)
                text = r.recognize_google(audio)
                break
            except:
                not_recognized()
    return text


def saying():
    engine.say("Sir I think you know your name, But yeah it Veselin!")
    engine.runAndWait()


def exit_command():
    engine.say("It was nice to help you Sir, See you soon!")
    engine.runAndWait()


def say_joke():
    joke = pick_joke()

    engine.say(joke)
    engine.runAndWait()


def play_song():
    song = pick_song()
    webbrowser.open(song, new=2)


def forecast():
    text = make_prediction()
    engine.say(text)
    engine.runAndWait()



