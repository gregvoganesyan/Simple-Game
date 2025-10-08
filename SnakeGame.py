#Gregory Oganesyan
#Jonathan Reyes
#Matthew Vasquez

import random

minutesRemaining = 5
randomNum = 0
food = "placeholder"

print(f"Congrats, you are now a snake, and you are trapped inside a house!")
print(f"You hear a hunter approaching and you have "+minutesRemaining+ "until the hunter catches you!")
print(f"You have to get to the LIVING ROOM before he finds you!")
print(f"However, you need energy to get to LIVING ROOM. You can choose to eat a BIRD, LIZARD, or RAT. Only one option will give you enough energy to make it...")
# make a while loop that does not break out until the user guesses the right random number
# if minutes remaining <1, then the game is over
while (food != "BIRD")
  randomNum = random.randomint(1,3)
  if randomNum = 1
    food = "BIRD"
  else if randomNUM = 2
    food = "LIZARD"
  else if randomNUM = 3
    food = "RAT"
  print(f"You have chosen... "+ food)
  if  food = "BIRD"
    printf()
  else if food = "LIZARD"
    minutesRemaining-=1
    


