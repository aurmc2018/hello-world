import random
import sys
# Create number to choice mapping
mapping = {
  1: "Rock",
  2: "Paper",
  3: "Scissors"
}
# Generate computer choice
pc_choice = random.randint(1, 3)
pc_choice_output = "I chose %s." % mapping[pc_choice]
# Request user choice
try:
  user_choice = int(input("Choose Rock (1), Paper (2), or Scissors (3): "))
  user_choice_output = "You chose %s." % mapping[user_choice]
except (ValueError, KeyError):
  print(pc_choice_output)
  print("You chose nothing.")
  print("You lose by default.")
  sys.exit(0)
# Share choices
print(pc_choice_output)
print(user_choice_output)
# Setup results
i_win = "%s beats %s - I win!" % (mapping[pc_choice], mapping[user_choice])
u_win = "%s beats %s - you win!" % (mapping[user_choice], mapping[pc_choice])
tie = "Tie!"

# Share winner
# if pc_choice == user_choice:
#   print(tie)
# elif pc_choice == 1: # Rock
#   if user_choice == 2: # Paper
#     print(u_win)
#   else: # Scissors
#     print(i_win)
# elif pc_choice == 2: # Paper
#   if user_choice == 1: # Rock
#     print(i_win)
#   else: # Scissors
#     print(u_win)
# else: # Scissors
#   if user_choice == 1: # Rock
#     print(u_win)
#   else: # Paper
#     print(i_win)

# Share results
if pc_choice == user_choice:
  print(tie)
elif (user_choice + 1) % 3 == pc_choice % 3:
  print(i_win)
else:
  print(u_win)