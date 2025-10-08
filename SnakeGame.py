#AUTHOR: Gregory Oganesyan
#AUTHOR: Jonathan Reyes
#AUTHOR: Matthew Vasquez

import random

minutesRemaining = 5
randomNum = 0
food = "placeholder"
userOption = 0

def getNumberFromUser(message):
    while True:
        userOption = input(message)
        try:
            num = int(userOption)
            return num
        except ValueError:
            print("Invalid input. Please enter a whole number.")
          
def main()
  print(f"Congrats, you are now a snake, and you are trapped inside a house!")
  print(f"You hear a hunter approaching and you have "+minutesRemaining+ "until the hunter catches you!")
  print(f"You have to get to the LIVING ROOM before he finds you!")
  print(f"However, you need energy to get to LIVING ROOM. You can choose to eat a BIRD, LIZARD, or RAT. Only one option will give you enough energy to make it...")
  # make a while loop that does not break out until the user guesses the right random number
  # if minutes remaining <1, then the game is over
  print(f"*********YOUR FOOD OPTIONS*********")
  print(f"1) BIRD")
  print(f"2) LIZARD")
  print(f"3) RAT")
  userOption = getNumberFromUser("ENTER THE NUMBER OF THE OPTION YOU WANT TO CHOOSE")
  print(f"You have entered "+userOption)
  while (food != "BIRD")
    randomNum = random.randomint(1,3)
    if randomNum == 1
      food = "BIRD"
    else if randomNUM == 2
      food = "LIZARD"
    else if randomNUM == 3
      food = "RAT"
    print(f"You have chosen... "+ food)
    if  food = "BIRD"
      printf()
    else if food = "LIZARD"
      minutesRemaining-=1
      if minutesRemaining<1
        print(f"NO!!! THE HUNTER HAS CAUGHT YOU!")
        print(f"GAME OVER")
        #the game ends if the time remaining is zero
        sys.exit()
      else if minutesRemaining == 1
        print(f"That was not enough energy to get your body to the living room!")
        print(f"The hunter is now "+ minutesRemaining + "minute remaining.")
        print(f"print(f"However, you need energy to get to LIVING ROOM. You can choose to eat a BIRD, LIZARD, or RAT. Only one option will give you enough energy to make it...")
      
    


