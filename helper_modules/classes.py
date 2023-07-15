"""All of the game modes (straight, box, straight/box), their parent class, and player class are here.
by patjcolon
last updated 7/15/2023"""

import random
from math import floor

class Player:
    """Maintains bet and cash amounts of player, allows player to change bet amount and add funds."""

    def __init__(self, cash:float = 1000):
        """Initializing, starts with no bet and however much cash the player has."""
        self.bet = 0
        self.cash = cash

    def display_cash(self):
        """Displays current total cash balance of player."""
        print(f"You have ${self.cash:,.2f}")

    def display_bet(self):
        """Displays current bet the player has set to make."""
        print(f"You are betting ${self.bet:,.2f}")


    def place_bet(self):
        """Allows player to change their bet amount to an integer between 1 and 10.
        Cash is not taken out until a round is started."""
        
        has_not_bet = True
        while has_not_bet == True:
            print(f"You have ${self.cash:,.2f}. Place your bet.")
            print("Minimum bet is $1. Maximum bet is $10.")
            string_player_bet = input("\nBet: $")
            try:
                player_bet = int(string_player_bet)
                if player_bet > 0 and player_bet < 11:
                    new_money = self.cash - player_bet
                    if new_money >= 0:
                        self.bet = player_bet
                        has_not_bet = False
                    else:
                        print(
                            f"You have ${self.cash:,.2f}. You cannot bet ${player_bet}.")
                else:
                    print(
                        f"${string_player_bet} is not within minimum and maximum range.")
            except ValueError:
                print(f"{string_player_bet} is not a valid bet.")

    def add_funds(self):
        """Allows the player to add any amount of money of at least 0.01 to their cash.
        Fractions of pennies are not accepted."""
        print("Enter amount you would like to add.")
        cash_added = False
        while not cash_added:
            cash_input = input("$").split(",")
            cash_input = ''.join(cash_input)        
        
            try:
                cash_input = float(cash_input)
                cash_amount = floor(cash_input * 100 + 0.00001)/100.0
                if cash_input != cash_amount:
                    print("Amount cannot include fractions of a penny.")
                if cash_amount < 0.01:
                    print("Amount must be at least 1 penny.")
                else: 
                    self.cash += cash_amount
                    print(f"${cash_amount:,.2f} added. Your balance is now ${self.cash:,.2f}")
                    cash_added = True
            except ValueError:
                print(f"{cash_input} is not a valid cash value.")


class GameMode:
    """Super class for all other Game Modes. Allows all game modes to pick 
    player numbers and get winning numbers.
    """

    def __init__(self):
        """Initializing empty lists for player numbers and winning numbers. Creates internal
        number_list that the player and computer can choose their numbers from."""
        self.player_numbers = []
        self.winning_numbers = []
        self.number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    def change_player_numbers(self):
        """Has player pick 3 numbers between 0-9 each, returns list of valid choices"""
        self.player_numbers = []
        select_which_num_text = ["first", "second", "third"]
        while len(self.player_numbers) < 3:
            print(f"Select your {select_which_num_text[len(self.player_numbers)]} number.")
            chosen_number = input("Pick a number between 0 and 9. \n>")
            try:
                chosen_number = int(chosen_number)
                if chosen_number in self.number_list:
                    print(f"Your {select_which_num_text[len(self.player_numbers)]} number is {chosen_number}.")
                    self.player_numbers.append(chosen_number)
                else:
                    print("Number not within valid range.")
            except ValueError:
                print("Number choice invalid.")

    def get_winning_numbers(self):
        """returns a list of 3 random numbers each between 0-9"""
        self.winning_numbers = []
        while len(self.winning_numbers) < 3:
            self.winning_numbers.append(random.choice(self.number_list))


class BoxMode(GameMode):
    """Box game mode that gets player numbers and winning numbers, sorts and compares, and pays 50x bet per win."""

    def play_box(self, player_bet: int):
        """Gets player numbers and winning numbers and sorts them. Compares for any order match and pays out 50x
        player bet if won."""
        prize_money = player_bet * 50
        
        self.change_player_numbers()
        self.get_winning_numbers()
        self.winning_numbers.sort()
        self.player_numbers.sort()

        print(f"Your numbers are: {self.player_numbers}."
        + f"\nThe winning numbers are: {self.winning_numbers}.")
        if self.player_numbers == self.winning_numbers:
            print("Congratulations! You won!")
            print(f"You earned ${prize_money:,.2f}!")
            return prize_money
        else:
            print("Sorry. Better luck next time.")
            return 0


class StraightMode(GameMode):
    """Straight game mode that gets player numbers and winning numbers, and pays 150x bet per win."""

    def play_straight(self, player_bet: int):
        """Gets player numbers and winning numbers. Compares for exact match to payout 150x player bet if won."""
        prize_money = player_bet * 150
        
        self.change_player_numbers()
        self.get_winning_numbers()

        print(f"Your numbers are: {self.player_numbers}."
        + f"\nThe winning numbers are: {self.winning_numbers}.")
        if self.player_numbers == self.winning_numbers:
            print("Congratulations! You won!")
            print(f"You earned ${prize_money:,.2f}!")
            return prize_money
        else:
            print("Sorry. Better luck next time.")
            return 0


class StraightBoxMode(GameMode):
    """Straight box plays like those game modes and pays out half their prizes, checking for straight win first."""

    def play_straight_box(self, player_bet: int):
        """Gets player numbers and winning numbers. Compares for exact match to payout 75x player bet if won.
        If no match, sorts both number lists then compares for any order match to payout 25x player bet if won."""
        straight_prize = player_bet * 75
        box_prize = player_bet * 25

        self.change_player_numbers()
        self.get_winning_numbers()

        print(f"Your numbers are: {self.player_numbers}."
        + f"\nThe winning numbers are: {self.winning_numbers}.")

        # checking for straight win
        if self.player_numbers == self.winning_numbers:
            print("Congratulations! You won!")
            print(f"You earned ${straight_prize:,.2f}!")
            return straight_prize
        
        # checking for box win
        self.winning_numbers.sort()
        self.player_numbers.sort()
        if self.player_numbers == self.winning_numbers:
            print("Congratulations! You won!")
            print(f"You earned ${box_prize:,.2f}!")
            return box_prize
        else:
            print("Sorry. Better luck next time.")
            return 0
