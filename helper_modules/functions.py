"""Contains helper functions and Player class. Helper functions
are display main menu, display game menu, and display rules.
by patjcolon
last updated 7/15/2023"""

# importing libraries
import os
from time import sleep



def display_main_menu():
    """Displays main menu."""
    os.system('cls')
    print("="*40)
    print("|| Welcome to PICK 3 LOTTO!           ||")
    print("="*40 + "\n")

    print("Options:")
    print("1) Pick 3: Straight")
    print("2) Pick 3: Box")
    print("3) Pick 3: Straight/Box")
    print("4) Add Cash")
    print("5) Rules \n \n")

    print("6) Quit")
    print("-"*40)
    print("\n")


def display_game_menu(game_selected:int = 1):
    """Displays game mode menu with unique text depending on mode selected."""
    game_mode_names = {1: "Straight!    ", 2: "Box!         ", 3: "Straight/Box!"}
    
    os.system('cls')
    print("="*40)                                #|
    print(f"|| PICK 3 {game_mode_names[game_selected]}               ||")
    print("="*40 + "\n")
    
    print("Options:")
    print("1) Play")
    print("2) Change Bet")
    print("3) Check Balance")
    print("4) Rules \n \n \n")

    print("5) Return to Main Menu")
    print("-"*40)
    print("\n")


def display_rules():
    """Displays rules of each game mode."""
    print("""
    PICK 3 LOTTO! Rules:
- Place a bet from $1-$10
- Pick 3 numbers from 0-9 and match them to the winning numbers.
Straight: If the winning numbers match in the same order, you win 150x your bet.
Box: If the winning numbers match in any order, you win 50x your bet.
Straight/Box: If winning numbers are an exact match, win 75x your bet.
    Or if the winning numbers match in any order, win 25x your bet.

You can play as many times as you would like, as long as you have the funds available.
Winning numbers are chosen by a pseudorandom number generator and are not fully random.
\n""")


def title_animation():
    """Displays the title animation for when the game is first loaded. Has 3 slides using a list."""
    title_slides = [
"""
 /$$$$$$$  /$$$$$$  /$$$$$$  /$$   /$$
| $$__  $$|_  $$_/ /$$__  $$| $$  /$$/
| $$  \ $$  | $$  | $$  \__/| $$ /$$/ 
| $$$$$$$/  | $$  | $$      | $$$$$/  
| $$____/   | $$  | $$      | $$  $$  
| $$        | $$  | $$    $$| $$\  $$ 
| $$       /$$$$$$|  $$$$$$/| $$ \  $$
|__/      |______/ \______/ |__/  \__/
""",

"""
 /$$$$$$$  /$$$$$$  /$$$$$$  /$$   /$$        /$$$$$$ 
| $$__  $$|_  $$_/ /$$__  $$| $$  /$$/       /$$__  $$
| $$  \ $$  | $$  | $$  \__/| $$ /$$/       |__/  \ $$
| $$$$$$$/  | $$  | $$      | $$$$$/           /$$$$$/
| $$____/   | $$  | $$      | $$  $$          |___  $$
| $$        | $$  | $$    $$| $$\  $$        /$$  \ $$
| $$       /$$$$$$|  $$$$$$/| $$ \  $$      |  $$$$$$/
|__/      |______/ \______/ |__/  \__/       \______/ 
""",

"""
 /$$$$$$$  /$$$$$$  /$$$$$$  /$$   /$$        /$$$$$$ 
| $$__  $$|_  $$_/ /$$__  $$| $$  /$$/       /$$__  $$
| $$  \ $$  | $$  | $$  \__/| $$ /$$/       |__/  \ $$
| $$$$$$$/  | $$  | $$      | $$$$$/           /$$$$$/
| $$____/   | $$  | $$      | $$  $$          |___  $$
| $$        | $$  | $$    $$| $$\  $$        /$$  \ $$
| $$       /$$$$$$|  $$$$$$/| $$ \  $$      |  $$$$$$/
|__/      |______/ \______/ |__/  \__/       \______/ 
                                                      
                                                      
                                                      
 /$$        /$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$  /$$ 
| $$       /$$__  $$|__  $$__/|__  $$__//$$__  $$| $$ 
| $$      | $$  \ $$   | $$      | $$  | $$  \ $$| $$ 
| $$      | $$  | $$   | $$      | $$  | $$  | $$| $$ 
| $$      | $$  | $$   | $$      | $$  | $$  | $$|__/ 
| $$      | $$  | $$   | $$      | $$  | $$  | $$     
| $$$$$$$$|  $$$$$$/   | $$      | $$  |  $$$$$$/ /$$ 
|________/ \______/    |__/      |__/   \______/ |__/ 
"""
]


    for slide in title_slides:
        os.system('cls')
        print(slide)
        sleep(0.4)
        
    input("\n           Press Enter to start!")
