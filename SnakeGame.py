# AUTHOR: Gregory Oganesyan
# AUTHOR: Jonathan Reyes

import random
import sys
import time
import os
import pygame
from colorama import Fore, Style, init
from PIL import Image
init(autoreset=True)


def slowPrintText(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def getNumberFromUser(message):
    while True:
        userOption = input(message)
        try:
            num = int(userOption)
            if 1 <= num <= 3:
                return num
            else:
                slowPrintText("Please enter a number from 1 to 3!", Fore.RED)
        except ValueError:
            slowPrintText("Invalid input. Please enter a whole number.", Fore.RED)

def livingMap(snake_pos=0):
    return [
        "+----------------------+",
        "|      ___             |",
        "|     |   |  ___       |",
        "|     |___| |   |      |",
        "|           |___|      |",
        "|                      |",
        f"|{' ' * snake_pos}🐍{' ' * (22 - snake_pos - 2)}|",
        "|                      |",
        "+----------------------+",
    ]

def frontMap(snake_pos=0):
    return [
        "+----------------------+",
        "|   ____               |",
        "|  |    |   ____       |",
        "|  |____|  |    |      |",
        "|          |____|      |",
        "|        🚪            |",
        f"|{' ' * snake_pos}🐍{' ' * (22 - snake_pos - 2)}|",
        "|                      |",
        "+----------------------+",
    ]

def backyardMap(snake_pos=0):
    return [
        "+----------------------+",
        "|   🌳                 |",
        "|       🪵             |",
        "|                      |",
        "|      🌿              |",
        "|                      |",
        f"|{' ' * snake_pos}🐍{' ' * (22 - snake_pos - 2)}|",
        "|                      |",
        "+----------------------+",
    ]

def animate(map_func):
    snake_frames = ["🐍", "🐍~", "🐍≈", "🐍-"]
    for pos in [0, 4, 8, 12, 16, 12, 8, 4, 0]:
        for frame in snake_frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            lines = map_func(snake_pos=pos)
            print("\n".join(lines))
            time.sleep(0.15)

def playmusic():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("congratulations.mp3")
        pygame.mixer.music.play()
    except:
        pass

def playWaitingMusic():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("waitingdecisionmusic.mp3")
        pygame.mixer.music.play(-1)
    except:
        pass

def stop_music():
    try:
        pygame.mixer.music.stop()
    except:
        pass

def main():
    minutesRemaining = 5
    correctFood = ""
    food = ""
    userOption = 0

    randomNum = random.randint(1, 3)
    if randomNum == 1:
        correctFood = "BIRD"
    elif randomNum == 2:
        correctFood = "LIZARD"
    elif randomNum == 3:
        correctFood = "RAT"

    snakeimg = r"""
           /^\/^\
         _|__|  O|
\/     /~     \_/ \
 \____|__________/  \
        \_______      \
                `\     \                 \
                  |     |                  \
                 /      /                    \
                /     /                       \\
              /      /                         \ \
             /     /                            \  \
           /     /             _----_            \   \
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~
"""

    print(snakeimg)
    snakesnack = r"""
                       _                               _    
        ___ _ __   __ _| | _____   ___ _ __   __ _  ___| | __
       / __| '_ \ / _` | |/ / _ \ / __| '_ \ / _` |/ __| |/ /
       \__ \ | | | (_| |   <  __/ \__ \ | | | (_| | (__|   < 
       |___/_| |_|\__,_|_|\_\___| |___/_| |_|\__,_|\___|_|\_\
"""
    print(snakesnack)
    slowPrintText("Congrats, you are now a snake, and you are trapped inside a house!", Fore.YELLOW)
    slowPrintText(f"You hear a hunter approaching and you have {minutesRemaining} minutes remaining until the hunter catches you!", Fore.YELLOW)
    slowPrintText("You have to get to the LIVING ROOM before he finds you!", Fore.YELLOW)
    slowPrintText("However, you need energy to get to the LIVING ROOM. You can choose to eat a BIRD, LIZARD, or RAT.", Fore.YELLOW)
    slowPrintText("Only one option will give you enough energy to make it...", Fore.YELLOW)

    playWaitingMusic()
    print("\n".join(livingMap()))

    while True:
        slowPrintText("*********YOUR FOOD OPTIONS*********", Fore.CYAN)
        slowPrintText("1) BIRD", Fore.CYAN)
        slowPrintText("2) LIZARD", Fore.CYAN)
        slowPrintText("3) RAT", Fore.CYAN)
        slowPrintText("***********************************", Fore.CYAN)
        userOption = getNumberFromUser("ENTER THE NUMBER OF THE OPTION YOU WANT TO CHOOSE: ")

        if userOption == 1:
            food = "BIRD"
        elif userOption == 2:
            food = "LIZARD"
        elif userOption == 3:
            food = "RAT"

        slowPrintText(f"You have chosen... {food}", Fore.MAGENTA)
        if food == correctFood:
            stop_music()
            slowPrintText(f"AMAZING! The {food} has given you enough energy to escape the LIVING ROOM!", Fore.GREEN)
            break
        else:
            animate(livingMap)
            minutesRemaining -= 1
            if minutesRemaining < 1:
                stop_music()
                slowPrintText("💀 NO!!! THE HUNTER HAS CAUGHT YOU!", Fore.RED)
                slowPrintText("GAME OVER", Fore.RED)
                sys.exit()
            elif minutesRemaining == 1:
                slowPrintText("That was not enough energy to get to the backyard!", Fore.RED)
                slowPrintText(f"The hunter is now {minutesRemaining} minute away!", Fore.RED)
            else:
                slowPrintText("That was not enough energy to get to the backyard!", Fore.RED)
                slowPrintText(f"The hunter is now {minutesRemaining} minutes away!", Fore.RED)

    randomNum = random.randint(1, 3)
    if randomNum == 1:
        correctFood = "BIRD"
    elif randomNum == 2:
        correctFood = "LIZARD"
    elif randomNum == 3:
        correctFood = "RAT"

    slowPrintText("Congrats, you are now a snake, and you are trapped inside a house!", Fore.YELLOW)
    slowPrintText(f"You hear a hunter approaching and you have {minutesRemaining} minutes remaining until the hunter catches you!", Fore.YELLOW)
    slowPrintText("You have to get to the LIVING ROOM before he finds you!", Fore.YELLOW)
    slowPrintText("However, you need energy to get to the LIVING ROOM. You can choose to eat a BIRD, LIZARD, or RAT.", Fore.YELLOW)
    slowPrintText("Only one option will give you enough energy to make it...", Fore.YELLOW)

    playWaitingMusic()
    print("\n".join(frontMap()))

    while True:
        slowPrintText("*********YOUR FOOD OPTIONS*********", Fore.CYAN)
        slowPrintText("1) BIRD", Fore.CYAN)
        slowPrintText("2) LIZARD", Fore.CYAN)
        slowPrintText("3) RAT", Fore.CYAN)
        slowPrintText("***********************************", Fore.CYAN)
        userOption = getNumberFromUser("ENTER THE NUMBER OF THE OPTION YOU WANT TO CHOOSE: ")

        if userOption == 1:
            food = "BIRD"
        elif userOption == 2:
            food = "LIZARD"
        elif userOption == 3:
            food = "RAT"

        slowPrintText(f"You have chosen... {food}", Fore.MAGENTA)
        if food == correctFood:
            stop_music()
            slowPrintText(f"AMAZING! The {food} has given you enough energy to escape the FRONT DOOR!", Fore.GREEN)
            break
        else:
            animate(frontMap)
            minutesRemaining -= 1
            if minutesRemaining < 1:
                stop_music()
                slowPrintText("💀 NO!!! THE HUNTER HAS CAUGHT YOU!", Fore.RED)
                slowPrintText("GAME OVER", Fore.RED)
                sys.exit()
            elif minutesRemaining == 1:
                slowPrintText("That was not enough energy to get to the backyard!", Fore.RED)
                slowPrintText(f"The hunter is now {minutesRemaining} minute away!", Fore.RED)
            else:
                slowPrintText("That was not enough energy to get to the backyard!", Fore.RED)
                slowPrintText(f"The hunter is now {minutesRemaining} minutes away!", Fore.RED)

    randomNum = random.randint(1, 3)
    if randomNum == 1:
        correctFood = "BIRD"
    elif randomNum == 2:
        correctFood = "LIZARD"
    elif randomNum == 3:
        correctFood = "RAT"

    slowPrintText("Congrats, you are now a snake, and you are trapped inside a house!", Fore.YELLOW)
    slowPrintText(f"You hear a hunter approaching and you have {minutesRemaining} minutes remaining until the hunter catches you!", Fore.YELLOW)
    slowPrintText("You have to get to the LIVING ROOM before he finds you!", Fore.YELLOW)
    slowPrintText("However, you need energy to get to the LIVING ROOM. You can choose to eat a BIRD, LIZARD, or RAT.", Fore.YELLOW)
    slowPrintText("Only one option will give you enough energy to make it...", Fore.YELLOW)

    playWaitingMusic()
    print("\n".join(backyardMap()))

    while True:
        slowPrintText("*********YOUR FOOD OPTIONS*********", Fore.CYAN)
        slowPrintText("1) BIRD", Fore.CYAN)
        slowPrintText("2) LIZARD", Fore.CYAN)
        slowPrintText("3) RAT", Fore.CYAN)
        slowPrintText("***********************************", Fore.CYAN)
        userOption = getNumberFromUser("ENTER THE NUMBER OF THE OPTION YOU WANT TO CHOOSE: ")

        if userOption == 1:
            food = "BIRD"
        elif userOption == 2:
            food = "LIZARD"
        elif userOption == 3:
            food = "RAT"

        slowPrintText(f"You have chosen... {food}", Fore.MAGENTA)
        if food == correctFood:
            stop_music()
            slowPrintText(f"AMAZING! The {food} has given you enough energy to escape to the BACKYARD!", Fore.GREEN)
            break
        else:
            animate(backyardMap)
            minutesRemaining -= 1
            if minutesRemaining < 1:
                stop_music()
                slowPrintText("💀 NO!!! THE HUNTER HAS CAUGHT YOU!", Fore.RED)
                slowPrintText("GAME OVER", Fore.RED)
                sys.exit()
            elif minutesRemaining == 1:
                slowPrintText("That was not enough energy to get to the backyard!", Fore.RED)
                slowPrintText(f"The hunter is now {minutesRemaining} minute away!", Fore.RED)
            else:
                slowPrintText("That was not enough energy to get to the backyard!", Fore.RED)
                slowPrintText(f"The hunter is now {minutesRemaining} minutes away!", Fore.RED)

    stop_music()
    slowPrintText("🎉 CONGRATS! YOU ESCAPED THE HUNTER AND MADE IT OUTSIDE! 🐍", Fore.GREEN)
    playmusic()
    congratsmsg = r"""
                                 _       
                                | |      
  ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
 / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
| (_| (_) | | | | (_| | | | (_| | |_\__ \
 \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                  __/ |                  
                 |___/                   
"""
    print(congratsmsg)
    time.sleep(10)

main()
