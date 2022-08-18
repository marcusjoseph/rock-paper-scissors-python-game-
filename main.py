import random

def get_choices():
  player_choice = input("Enter a choice (Rock , Paper, Scissors:")
  options= ["rock", "papper", "scissors"]
  computer_choice= random.choice(options)
  choices = {"player": player_choice, "computer": 
  computer_choice}
  
  return choices

def check_win(player, computer):
  print(f"you Choice {player}, computer Choice {computer}")
  if player == computer:
    return "it is a tie!"
  elif player == "rock":
    if computer == "scissors":
     return "rock Smashes scissors! You win"
    else:
      return "Paper covers rock! YOu lose."
  elif player == "paper":
    if computer == "rock":
     return "paper covers rocks! you win!"
    else:
      return "scissors cuts paper! you Lose."
  elif player == "scissors":
    if computer == "paper":
     return "scissors cuts paper! You win!"
    else:
      return "rocks smashes scissors! YOu lose."


choices = get_choices()
result = check_win(choices["player"], choices["computer"] )
print(result)