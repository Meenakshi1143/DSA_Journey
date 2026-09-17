'''
random module - helps to generate random values
OTP generations, Story Generation, Games(Rock Paper Scissiors), Number Guessing

'''

import random, time

'''
#random number generation - OTP (Time module helps to use time functions)
#a = random.randint(1000, 9999)
#print(a)

for i in range (5):
    time.sleep(1) #sleep(Seconds) - helps for a waiting period
    print(random.randint(1000, 9999))

#Playing a Game (Rock Paper Scissors)
#Two Players - game -

player1 = input("Enter one of these - Rock, paper, Scissors: ").lower().strip()
player2 = random.choice(["Rock" ,"Paper", "Scissors"]).lower()
print(f"Player1: {player1}, Player2: {player2}")
if player1 == "Rock" and player2 == "Paper":
    print("Player2 Won")
elif player1 == "paper" and player2 == "Scissors":
    print("Player1Won")
elif player1 == "Scissor" and player2 == "Rock":
    print("Player2 Won")
elif player1 == player2 :
    print("Tie")
else:
    print("Player1 won")
    
#Task - Get the score for each user and declare the winner
#play the game for 10 times

#Task2 - Give user a choice - 1. RPS, 2. NG, 3. Study, 4. Any Number

when = ['A long back', 'Once upon a time', 'Few Years ago']
who = ['Devara', 'King in the France', 'Barbie Queen']
what = ['A Magical Sword', 'Powerful Hammer', 'Unlimited Arrows']
where = ['Far in the Galaxy', 'End of Ocean', 'in india']
how = ['War Started', 'Both fought for 15days', 'Sad Ending']
#To create a story - link when to what to who to how...
print(random.choice(when) + " " + random.choice(who))


#Business Card generator - name, email id, mobile number, website link
#segno - pip install segno
import segno
print(dir(segno))
from segno import helpers
qr = helpers.make_mecard(name = "Meenakshi",
                         email = "meenav1143@gmail.com",
                         phone = "+91 7671957601",
                         url = "https://github.com/Meenakshi1143")

print(qr)
                    
qr.save("mycard.png", scale = 10)

        

#Build a virtual assistant using python - virtual environmet
#Speak, respond back, Greet you, Make a conversation, Open Broweser, Loacte Google Maps, tell a story, Play a game.....
#POP - Functions, Control Block



player1_score, player2_score = 0, 0
n = int(input("Enter Number: "))
for i in range(n):
    print(f"Round {i + 1}: ")
    player1 = input("Enter one of these - Rock, paper, Scissors: ").lower().strip()
    player2 = random.choice(["Rock" ,"Paper", "Scissors"]).lower()

        
    print(f"Player1: {player1}, Player2: {player2}")
    if player1 == player2:
        print("Tie")
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper"):
        print("Player 1 Won!")
        player1_score += 1
    
    else:
        print("Player2 won")
        player2_score += 1
        
print("\n----- FINAL SCORE -----")
print("Player 1:", player1_score)
print("Player 2:", player2_score)

if player1_score > player2_score:
    print("Player 1 is the Winner!")
elif player2_score > player1_score:
    print("Player2 is the Winner!")
else:
    print("Match Tie!")
'''



#Task2 - Give user a choice - 1. RPS, 2. NG, 3. Study, 4. Any Number
import random

def rps():
    player1_score, player2_score = 0, 0
    n = int(input("Enter Number: "))
    for i in range(n):
        print(f"Round {i + 1}: ")
        player1 = input("Enter one of these - Rock, paper, Scissors: ").lower().strip()
        player2 = random.choice(["Rock" ,"Paper", "Scissors"]).lower()

            
        print(f"Player1: {player1}, Player2: {player2}")
        if player1 == player2:
            print("Tie")
        elif (player1 == "rock" and player2 == "scissors") or \
             (player1 == "paper" and player2 == "rock") or \
             (player1 == "scissors" and player2 == "paper"):
            print("Player 1 Won!")
            player1_score += 1
        
        else:
            print("Player2 won")
            player2_score += 1
            
    print("\n----- FINAL SCORE -----")
    print("Player 1:", player1_score)
    print("Player 2:", player2_score)

    if player1_score > player2_score:
        print("Player 1 is the Winner!")
    elif player2_score > player1_score:
        print("Player2 is the Winner!")
    else:
        print("Match Tie!")

def number_guessing():
    print("\n--- Number Guessing Game ---")
    number = random.randint(1, 10)
    for i in range(3):
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == number:
            print("Correct! You won!")
            break
        elif guess > number:
            print("Too High!")
        else:
            print("Too Low!")
        print("Attempts left:", 2 - i)
    else:
        print("You lost!")
        print("The number was:", number)

def study():
    print("\n--- Study ---")
    subject = input("What subject do you want to study? ")
    print(f"All the best! Keep learning {subject}!")

print("----- MENU -----")

print("1. Rock Paper Scissors")
print("2. Number Guessing")
print("3. Study")
choice = input("Enter your choice (1/2/3): ")
if choice == "1":
    rps()
elif choice == "2":
    number_guessing()
elif choice == "3":
    study()
else:
    print("Invalid choice. Please select only 1, 2, or 3.")

