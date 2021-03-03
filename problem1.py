"""
----------------------------------------------------------------------
Name:   problem1.py

Purpose:  Ask the user how many wins and losses they have of 6 games. Then determine, based on the number of wins, what group they will be placed in. 
 
Author: Sinclair.K
 
Created:  03/03/2021
----------------------------------------------------------------------
"""

# program header
print ("****What Group Your Team is in Based on Your Number of Wins****")
print (" ")

# set initial value of wins
wins = 0

# instruct user to enter W or L
print ("Enter wins and losses for your team (W/L): ")

# use a loop to get user input and determine how many wins 
for games in range(6):
  wins_and_losses = input(" ")
  if wins_and_losses == "W":
    wins = wins + 1
  else:
    wins = wins

# determine what group the user is in based on wins
if wins >=5:
  print ("Your team is in Group 1.")
elif wins >=3:
  print ("Your team is in Group 2.")
elif wins >=1:
  print ("Your team is in Group 3.")
else:
  print ("Your team is eliminated from the tournament.")
  