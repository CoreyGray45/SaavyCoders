# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
# Do not just google the game and copy paste, If you would like to look at a completed version if you get stuck on a step please do so.
#Write your code below this line:
import random

choices = ("rock", "paper", "scissor")

# Define the rules
rules = ("rock">"scissor","paper">"rock","scissor">"paper")

person = input("Choose rock, paper or scissor: ").lower()

if person not in choices:
    print("Invalid choice. Try again.")

computer = random.choice(choices)

print(f"Computer chose {computer}")

if person == computer:
    print("Tie! Try Again")
elif person>computer:
    print("You win.")
else:
    print("You lose.")

print("The game is over.")












