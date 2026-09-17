'''
gTTS - Google text-to-speech

3-Functions
1. listen (speech recognition)
2. respond (gtts)
3. Assistant - conversation 


from gtts import gTTS
import playsound
#text =  gTTS("Once upon a time, a little girl found a magical key in her garden. She used the key to open a hidden door behind a tree. Inside, she found a room full of beautiful stars. She smiled and realized that magic can be found anywhere.")
text = gTTS("Hellooo! Good Morning! Hope you’re having a wonderful day!")
#text.save("audio.mp3")

playsound.playsound("audio.mp3")
'''
'''
from gtts import gTTS
import os
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr

#let us create listen function
def listen():
    """Function for Speech Recognition"""
    r = sr.Recognizer()
    #we will take microphone as source
    with sr.Microphone() as source:
        print("Start talking now")
        audio = r.listen(source, phrase_time_limit = 10)
    #We need to give our text as voice
    data = ""
    #Here we will give exceptions (try, except)
    try:
        data = r.recognize_google(audio)
        print("You said: ", data)
    except sr.UnknownValueError as e:
        print("Request Failed")
    except sr.RequestError as e:
        print("Speack clearly request is failing")
    return data
    #tts = gTTS(data)

    #tts.save("new.mp3")
    #playsound.playsound("new.mp3")

#listen()     

def respond(String):
    """Function to respond back"""
    print(String)
    tts = gTTS(String)
    tts.save("Speech.mp3")
    #We are using uuid - to randomize the content in the audio file
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#Here we will make our virtual assistant into action
def va(data):
    """Our Virtual Assistant withthe actions"""
    if "how are you" in data:
        listening = True
        respond("I'm fine thanks for asking.")
    elif "what are your plans" in data:
        listening = True
        respond("Only Study... One focus in 2026")
    elif "how are things going" in data:
        listening = True
        respond("Going somewhere")
    elif "time" in data:
        listening = True
        respond(time.ctime())
    elif "stop talking" in data:
        listening = False
        respond("Okay byeee")
    try:
        return listening
    except UnboundLocalError as e:
        print("Make Sure to speak louder and faster")
        
respond("Hey Meenakshiiiii.. Good to hear from you. How are you?")
listening = True
while listening:
    data = listen()
    listening = va(data)
'''


from gtts import gTTS
import os
import playsound
import time
import webbrowser
import uuid
import segno
import random
import speech_recognition as sr

#let us create listen function
def listen():
    """Function for Speech Recognition"""
    r = sr.Recognizer()
    #we will take microphone as source
    with sr.Microphone() as source:
        print("Start talking now")
        audio = r.listen(source, phrase_time_limit = 10)
    #We need to give our text as voice
    data = ""
    #Here we will give exceptions (try, except)
    try:
        data = r.recognize_google(audio)
        print("You said: ", data)
    except sr.UnknownValueError as e:
        print("Request Failed")
    except sr.RequestError as e:
        print("Speack clearly request is failing")
    return data
    #tts = gTTS(data)

    #tts.save("new.mp3")
    #playsound.playsound("new.mp3")

#listen()     

def respond(String):
    """Function to respond back"""
    print(String)
    tts = gTTS(String)
    #tts.save("Speech.mp3")
    #We are using uuid - to randomize the content in the audio file
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def rps():
    """Rock Paper Scissors Game using Voice"""

    player1_score = 0
    player2_score = 0

    respond("How many rounds do you want to play?")
    n = int(listen())

    for i in range(n):
        respond(f"Round {i + 1}. Say Rock, Paper, or Scissors.")

        player1 = listen().lower().strip()

        # Check valid input
        while player1 not in ["rock", "paper", "scissors"]:
            respond("Invalid choice. Please say Rock, Paper, or Scissors.")
            player1 = listen().lower().strip()

        player2 = random.choice(["rock", "paper", "scissors"])

        print(f"Player 1: {player1}")
        print(f"Player 2: {player2}")

        respond(f"I chose {player2}.")

        if player1 == player2:
            print("Tie!")
            respond("It's a tie!")

        elif (
            (player1 == "rock" and player2 == "scissors")
            or
            (player1 == "paper" and player2 == "rock")
            or
            (player1 == "scissors" and player2 == "paper")
        ):
            print("Player 1 Won!")
            respond("You won this round!")
            player1_score += 1

        else:
            print("Player 2 Won!")
            respond("I won this round!")
            player2_score += 1

    print("\n----- FINAL SCORE -----")
    print("You:", player1_score)
    print("Virtual Assistant:", player2_score)

    respond(
        f"The final score is You {player1_score}, "
        f"and me {player2_score}."
    )

    if player1_score > player2_score:
        respond("Congratulations! You won the game!")
    elif player2_score > player1_score:
        respond("I won the game!")
    else:
        respond("The game is a tie!")

def number_game():
    """Number Guessing Game using Voice"""

    number = random.randint(1, 10)

    for i in range(3):

        respond("Guess a number between 1 and 10")

        guess = listen()

        if guess == "":
            respond("Please say the number again")
            continue

        try:
            guess = int(guess)

        except ValueError:
            respond("Please say a number")
            continue

        if guess == number:
            respond("Correct! You won!")
            break

        elif guess > number:
            respond("Too High!")

        else:
            respond("Too Low!")

    else:
        respond(f"You lost! The number was {number}")


#Here we will make our virtual assistant into action
def va(data):
    """Our Virtual Assistant withthe actions"""
    listening = True
    if "how are you" in data:
        respond("I'm fine thanks for asking.")
    elif "what are your plans" in data:
        respond("Only Study... One focus in 2026")
    elif "how are things going" in data:
        respond("Going somewhere")
    elif "tell me about meghana" in data:
        respond("short girl with long hair and high attitude")
    elif "what is the time now" in data:
        respond(time.ctime())

    elif "open Google" in data:
        respond("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open location" in data:
        respond("Opening Location")
        webbrowser.open("https://www.google.com/maps/search/" + data.replace("locate",""))
        print("Located")
        
    elif "open Youtube" in data:
        respond("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        
    elif "open LinkedIn" in data:
        respond("Opening LinkedIn")
        webbrowser.open("httpsqq://www.linkedin.com/in/meenakshi-viyyapu-b9a161257/")

    elif "play RPS" in data:
        respond("Sure! Let's play Rock Paper Scissors.")
        rps()
    elif "play number game" in data:
        respond("Let's play number guessing game.")
        rps()
        
    elif "stop talking" in data:
        listening = False
        respond("Okay, byeee Meenaaa! See you later")
    try:
        return listening
    except UnboundLocalError as e:
        print("Make Sure to speak louder and faster")
        
respond("Hey Meenakshiiiii.. Good to hear from you. How are you?")
listening = True
while listening:
    data = listen()
    listening = va(data)



