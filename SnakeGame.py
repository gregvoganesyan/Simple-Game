# AUTHOR: Gregory Oganesyan
# AUTHOR: Jonathan Reyes

import random
import sys
import time
import os
import pygame
from colorama import Fore, Style, init

init(autoreset=True)

def slow_print(text, color=Fore.WHITE, delay=0.03):
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
                slow_print("Please enter a number from 1 to 3!", Fore.RED)
        except ValueError:
            slow_print("Invalid input. Please enter a whole number.", Fore.RED)


def create_living_room_map(snake_pos=0):
    lines = [
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
    return lines

def create_front_door_map(snake_pos=0):
    lines = [
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
    return lines

def create_backyard_map(snake_pos=0):
    lines = [
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
    return lines


def animate_snake(map_func):
    snake_frames = ["🐍", "🐍~", "🐍≈", "🐍-"]

    for pos in [0, 4, 8, 12, 16, 12, 8, 4, 0]:
        for frame in snake_frames:
            # clear old map
            os.system('cls' if os.name == 'nt' else 'clear')
            map_lines = map_func(snake_pos=pos)
            map_lines[6] = map_lines[6][:1+pos] + frame + map_lines[6][1+pos+len(frame):]
            print("\n".join(map_lines))
            time.sleep(0.15)

def playmusic():
    pygame.mixer.init()
    pygame.mixer.music.load("congratulations.mp3")
    pygame.mixer.music.play()

def playWaitingMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("waitingdecisionmusic.mp3")
    pygame.mixer.music.play(-1)

def play_round(minutesRemaining, round_name, map_func):
    food = ""
    correctFood = random.choice(["BIRD", "LIZARD", "RAT"])

    slow_print(f"\nYou are a snake trapped inside a house!", Fore.YELLOW)
    slow_print(f"You hear a hunter approaching. You have {minutesRemaining} minutes until he catches you.", Fore.YELLOW)
    slow_print(f"Reach the {round_name} by choosing the right food!\n", Fore.YELLOW)

    playWaitingMusic()
    
    map_lines = map_func(snake_pos=0)
    print("\n".join(map_lines))

    while True:
        slow_print("*********YOUR FOOD OPTIONS*********", Fore.CYAN)
        slow_print("1) BIRD", Fore.CYAN)
        slow_print("2) LIZARD", Fore.CYAN)
        slow_print("3) RAT", Fore.CYAN)
        slow_print("***********************************", Fore.CYAN)

        userOption = getNumberFromUser("ENTER THE NUMBER OF THE OPTION YOU WANT TO CHOOSE: ")

        if userOption == 1:
            food = "BIRD"
        elif userOption == 2:
            food = "LIZARD"
        elif userOption == 3:
            food = "RAT"

        slow_print(f"You have chosen... {food}\n", Fore.MAGENTA)

        if food == correctFood:
            pygame.mixer.music.stop()
            slow_print(f"✅ The {food} gave you enough energy to escape the {round_name}!", Fore.GREEN)
            time.sleep(1)
            break
        else:
            minutesRemaining -= 1
            if minutesRemaining < 1:
                pygame.mixer.music.stop()
                slow_print(f"💀 NO!!! THE HUNTER HAS CAUGHT YOU!", Fore.RED)
                slow_print(f"GAME OVER", Fore.RED)
                sys.exit()
            else:
                slow_print(f"❌ The {food} didn’t help! {minutesRemaining} minutes left...", Fore.RED)
                animate_snake(map_func)

    return minutesRemaining

def main():
    minutesRemaining = 5

    # Round 1: Living Room
    minutesRemaining = play_round(minutesRemaining, "LIVING ROOM", create_living_room_map)

    # Round 2: Front Door
    minutesRemaining = play_round(minutesRemaining, "FRONT DOOR", create_front_door_map)

    # Round 3: Backyard
    minutesRemaining = play_round(minutesRemaining, "BACKYARD", create_backyard_map)

    slow_print("\n🎉 CONGRATS! YOU ESCAPED THE HUNTER AND MADE IT OUTSIDE! 🐍", Fore.GREEN)
    playmusic()
    time.sleep(10)

if __name__ == "__main__":
    main()
