import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
rd = (random.randint(0,10))

""" initializing speak function for taking voice command"""

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



""" this function wish the user according to current time """
def wishme2():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir.")

    elif hour>=12 and hour<16:
        speak("good afternoon sir.")

    elif hour>=16 and hour<22:
        speak("good evening sir.")

    else:
        speak("good night sir.")

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir. i am Jarvis, how may i help you ")

    elif hour>=12 and hour<16:
        speak("good afternoon sir. i am Jarvis, how may i help you")

    elif hour>=16 and hour<22:
        speak("good evening sir. i am Jarvis, how may i help you?")

    else:
        speak("good night sir. i am Jarvis, how may i help you")

""" this function use for getting command from user as an voice through microphone"""
def takeCommand():
    #it take mic input from user a
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said :{query}")

    except Exception as e:
        speak("say that again please..")
        return "none"
    return query


def addition():
    print("enter how many number you want to add")
    totalsub = int(input(speak("enter how many number you want to add\n")))
    a=1
    sum=0
    while(a<=totalsub):
        sublist = int(input(speak(f"enter number {a} \n")))
        a = a+1
        sum += sublist
    speak(f"the sum of your numbers is {sum}")



def substraction():
    print("enter how many number you want to subtract")
    totalsub = int(input(speak("enter how many number you want to subtract\n")))
    a=1
    sub=0
    while(a<=totalsub):
        sublist = int(input(speak(f"enter number {a} \n")))
        a = a+1
        sub -= sublist
    speak(f"the substractioon of your numbers is {sub}")

def division():
    print("enter how many number you want to devide")
    totalsub = int(input(speak("enter how many number you want to add\n")))
    a=1
    div=1
    while(a<=totalsub):
        sublist = int(input(speak(f"enter number {a} \n")))
        a = a+1
    div /= sublist
    speak(f"the division of your numbers is {div}")

def multiplication():
    print("enter how many number you want to multiply")
    totalsub = int(input(speak("enter how many number you want to multiply\n")))
    a=1
    mul=1
    while(a<=totalsub):
        sublist = int(input(speak(f"enter number {a} \n")))
        a = a+1
        mul *= sublist
    speak(f"the multiplication of your numbers is {mul}")


def RPS():
    speak("enter your choice")
    user_action =(input("Enter a choice (rock, paper, scissor): "))
    possible_actions = ["rock", "paper", "scissor"]
    computer_action = random.choice(possible_actions)
    speak(f"\nYou choose {user_action}, I choose {computer_action}.\n")

    if user_action == computer_action:
        speak(f"you and I selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissor":
            speak("Rock smashes scissor! You win!")
        else:
            speak("Paper covers rock! yay! I win")
    elif user_action == "paper":
        if computer_action == "rock":
            speak("Paper covers rock! You win!")
        else:
            speak("Scissors cuts paper! yay! I win.")
    elif user_action == "scissor":
        if computer_action == "paper":
            speak("Scissors cuts paper! You win!")
        else:
            speak("Rock smashes scissors! yay! I win.")

    speak("do you want to play again")

def youtube():
    speak("this is what i found on youtube")
    youtube = query.replace("youtube","")
    web = "https://www.youtube.com/results?search_query=" + youtube
    webbrowser.open(web)

def google():
    speak("this is waht i found on google")
    google = query.replace("google","")
    web = "https://www.google.com/search?q=" + google
    webbrowser.open(web)

def openCdrive():
    speak("okay sir")
    folder = (f"C:\\{repl}")
    .startfile(folder)

def openDdrive():
    speak("sure sir")
    folderd = (f"D:\\{replace}")
    .startfile(folderd)

def spotify():
    spotify = query.replace("spotify","")
    speak(f"searching {spotify} in spotify")
    speak("this is what i found ")
    web = "https://open.spotify.com/search/" + spotify
    webbrowser.open(web)



    """ this is main function where the given command is performed by the computer"""

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=5)
            speak('according to wikipedia')
            print(results)
            speak(results)

        elif 'i am fine' in query:
            speak("nice to hear that")

        elif 'youtube' in query:
            speak("opening youtube")
            youtube()

        elif "google" in query:
            speak("opening google")
            google()

        elif "goodbye" in query:
            speak("good bye have a nice day sir")
            break

        elif "thank you" in query:
            speak("welcome")

        elif "spotify" in query :
            spotify()

        elif "the time" in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the current time is  {Time}")

        elif "date" in query:
            Date = datetime.datetime.today().date()
            speak(f"todays date is {Date}")

        elif "open vs code" in query:
            vsCode = "C:\\Users\\pk\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening vsCode")
            .startfile(vsCode)

        elif "open wps office" in query:
            wps= "C:\\Users\\pk\\AppData\\Local\\Kingsoft\\WPS Office\\ksolaunch.exe"
            speak("opening wps office")
            .startfile(wps)

        elif "play hindi song" in query:
            music = "C:\\hindi songs"
            songs = .listdir(music)
            .startfile(.path.join(music,songs[rd]))

        elif "play western song" in query:
            westernSong = "C:\\western songs"
            west = .listdir(westernSong)
            .startfile(.path.join(westernSong,west[rd]))

        elif "who are you" in query:
            speak("Allow me to introduce myself, I am Jarvis,"
                  "the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can,")

        elif "wish me according to time" in query:
            wishme2()

        elif "you are little bit late" in query:
            speak("sorry for you're inconvienience this is not my fault, i am new here, i need time to be more perfect")

        elif "it's okay" in query:
            speak("thanks for understanding sir")

        elif "do addition for me" in query:
            addition()

        elif "do subtraction for me" in query:
            substraction()

        elif "do multiplication for me" in query:
            multiplication()

        elif "division for me" in query:
            division()

        elif "play rps" in query:
            speak("okay sir")
            RPS()

        elif "yes i want to play again" in query:
            speak("sure why not")
            RPS()

        elif "no i don't want to play again" in query:
            speak("okay, thanks for playing")

        elif "drive" in query:
            repl = query.replace("drive","")
            openCdrive()

        elif "volume" in query:
            replace = query.replace("volume","")
            openDdrive()

        elif "news" in query:
            from NewsRead import latest_news
            latest_news()

