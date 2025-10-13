#AUTHOR: Gregory Oganesyan
#AUTHOR: Jonathan Reyes
#AUTHOR: Matthew Vasquez

import random
import sys

def getNumberFromUser(message):
    while True:
        userOption = input(message)
        try:
            num = int(userOption)
            if 1 <= num <= 3:
                return num
            else:
                print("Please enter a number from 1 to 3!")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
          
def main():
    minutesRemaining = 5
    correctFood = ""
    food=""
    userOption = 0
    
    randomNum = (random.randint(1, 3))

    if  randomNum == 1:
          correctFood = "BIRD"
    elif randomNum == 2:
          correctFood = "LIZARD"
    elif randomNum == 3:
          correctFood = "RAT"
    
    print("Congrats, you are now a snake, and you are trapped inside a house!")
    print("\nYou hear a hunter approaching and you have "+str(minutesRemaining)+ " minutes remaining until the hunter catches you!")
    print("You have to get to the LIVING ROOM before he finds you!")
    print("However, you need energy to get to the LIVING ROOM. You can choose to eat a BIRD, LIZARD, or RAT. Only one option will give you enough energy to make it...\n")
    
    while True:
        print("*********YOUR FOOD OPTIONS*********")
        print("1) BIRD")
        print("2) LIZARD")
        print("3) RAT")
        print("***********************************")
        userOption = getNumberFromUser("ENTER THE NUMBER OF THE OPTION YOU WANT TO CHOOSE: ")

        if userOption == 1:
          food = "BIRD"
        elif userOption == 2:
          food = "LIZARD"
        elif userOption == 3:
          food = "RAT"
        print(f"You have chosen... "+ food +"\n")
        if  food==correctFood:
            print(f"AMAZING! the "+food+" has given you enough energy to escape the LIVING ROOM")
            break
        elif food != correctFood:
            minutesRemaining-=1
            if minutesRemaining<1:
                print(f"NO!!! THE HUNTER HAS CAUGHT YOU!")
                print(f"GAME OVER")
                #the game ends if the time remaining is zero
                sys.exit()
            elif minutesRemaining == 1:
                print(f"That was not enough energy to get your body to the living room!")
                print(f"The hunter is now "+ str(minutesRemaining) + " minute remaining.")
                print(f"You need energy to get to the LIVING ROOM. You can choose to eat a BIRD, LIZARD, or RAT. Only one option will give you enough energy to make it...")
            else:
                print(f"That was not enough energy to get your body to the living room!")
                print(f"The hunter is now "+ str(minutesRemaining) + " minutes remaining.")
                print(f"You need energy to get to the LIVING ROOM. You can choose to eat a BIRD, LIZARD, or RAT. Only one option will give you enough energy to make it...")

    #the user has successfully completed the first round and guessed the correct food. Now the correct food is randomized again
    randomNum = (random.randint(1, 3))

    if  randomNum == 1:
          correctFood = "BIRD"
    elif randomNum == 2:
          correctFood = "LIZARD"
    elif randomNum == 3:
          correctFood = "RAT"

    print("\n\nCongrats, you made it out of the LIVING ROOM, but you are still trapped inside a house!")
    print("\nYou hear the hunter approaching and you have "+str(minutesRemaining)+ " minutes remaining until the hunter catches you!")
    print("You have to get to the FRONT DOOR before he finds you!")
    print("However, you need energy to get to the FRONT DOOR. You can choose to eat a BIRD, LIZARD, or RAT. Only one option will give you enough energy to make it...\n")
    
    while True:
        #same thing as above but now it is a different round

    #the user has successfully completed the second round and guessed the correct food. Now the correct food is randomized again for the last round
    randomNum = (random.randint(1, 3))

    if  randomNum == 1:
          correctFood = "BIRD"
    elif randomNum == 2:
          correctFood = "LIZARD"
    elif randomNum == 3:
          correctFood = "RAT"
    
    print("\n\nCongrats, you made it out of the FRONT DOOR, but you are still trapped inside a house!")
    print("\nYou hear the hunter approaching and you have "+str(minutesRemaining)+ " minutes remaining until the hunter catches you!")
    print("You have to get to the BACKYARD before he finds you!")
    print("However, you need energy to get to the BACKYARD. You can choose to eat a BIRD, LIZARD, or RAT. Only one option will give you enough energy to make it...\n")
    
    while True:
        #same thing as above but now it is a different round


main()


