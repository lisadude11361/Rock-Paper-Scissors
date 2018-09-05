from random import choice
from time import sleep

version = "0.7.1"

print("Rock, Paper, Scissors by Lisa")
sleep(1)
print("Version {}".format(version))
sleep(0.5)
print("\n")

print("~~~~~~~~~~~~~")
print("|    Rock   |")
print("|~~~~~~~~~~~|")
print("|    Paper  |")
print("|~~~~~~~~~~~|")
print("|  Scissors |")
print("~~~~~~~~~~~~~")

player = input("Rock (r), paper (p), or scissors (s)? ")

options = ["r", "p", "s"]
chosen = str(choice(options))
if chosen == "r":
    print("Rock")
    cpu = "Rock"
elif chosen == "p":
    print("Paper")
    cpu = "Paper"
elif chosen == "s":
    print("Scissors")
    cpu = "Scissors"


if player == 'r' or 'R':
    print("Rock vs {}".format(cpu))
elif player == 'p' or 'P':
    print("Paper vs {}".format(cpu))
elif player == 's' or 'S':
    print("Scissors vs {}".fomrat(cpu))
else:
    print("Invalid")
one = "Rock"
two = "Paper"
three = "Scissors"

if player == chosen:
    print("Draw")
elif player == 's' and chosen == 'r':
    print("Computer wins!")
elif player == 'r' and chosen == 's':
    print("Player wins!")
elif player == 'p' and chosen == 's':
    print("Computer wins!")
elif player == 's' and chosen == 'p':
    print("Player wins!")
