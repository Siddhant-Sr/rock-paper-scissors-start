import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_choices = ["rock" , "scissors", "paper"]
user_choice = input("What do you choose? Press R for rock S for sccissors, P for paper ")
comp = random.choice(computer_choices)

if user_choice == "R":
  print(f"Your choice is Rock\n {rock}" )
  if comp == "rock":
    print(f"Computer chooses rock\n {rock}" )
    print("Match is draw")
  elif comp == "scissors":
    print(f"Computer chooses scissors\n {scissors}" )
    print("You win")
  else:
    print(f"Computer chooses paper\n {paper}")
    print("You loose")

elif user_choice == "S":
    print(f"Your choice is Scissors\n {scissors}" )
    if comp == "rock":
      print(f"Computer chooses rock\n {rock}" )
      print("You loose")
    elif comp == "scissors":
      print(f"Computer chooses scissors\n {scissors}" )
      print("match is draw")
    else:
      print(f"Computer chooses paper\n {paper}")
      print("You win")

elif user_choice == "P":
  print(f"Your choice is Paper\n {paper}" )
  if comp == "rock":
    print(f"Computer chooses rock\n {rock}" )
    print("You win")
  elif comp == "scissors":
    print(f"Computer chooses scissors\n {scissors}" )
    print("You loose")
  else:
    print(f"Computer chooses paper\n {paper}")
    print("match is draw")








