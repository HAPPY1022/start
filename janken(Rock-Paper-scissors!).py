import random
print("Let's play Rock-Paper-Scissors!")
hands = ["rock","scissors","paper"]
while True:
  Player = input("choose your hand (rock,scissors,paper):").lower()
  if Player not in hands:
    print("Please enter a valid hands!")
    continue
  computer = random.choice(hand)
  print(f"The computer Played{computer}!")
  if Player == computer:
    print("It's a tie! Let's play again!")
  elif((player == "rock" and computer == "scissors") or 
       (player == "scissors" and computer == "paper") or
       (player == "paper" and computer == "rock")):
         print("You win! Congratulations!")
         break
  elif Player == computer:
    print("It's a tie! Let's play again!")
  else:
    print("You lose! Try again!")
    break
