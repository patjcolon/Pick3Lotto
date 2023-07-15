"""A gambling game based on California's Daily 3 brought to life using Python and PRNG
Takes functions and classes from the other modules and uses them here in a loop to play the game.
by patjcolon
Last updated 7/15/2023"""

from helper_modules import classes, functions


def main():
    """Loops the game for the player until they quit."""
    functions.title_animation()
    player = classes.Player(2417.56)
    
    while True:
        functions.display_main_menu()
        player.display_cash()
        menu_selection = input("\n> ")
        
        # Play Straight
        if menu_selection == '1':
            game = classes.StraightMode()

            while True:
                if player.cash <= 0:
                    print(f"You have ${player.cash:,.2f}. You do not have enough money to play.")
                    print("Returning to Main Menu.")
                    input("Press Enter to continue.")
                    break
            
                functions.display_game_menu(1)
                player.display_bet()

                menu_selection = input("\n> ")
                
                if menu_selection == '1':
                    if player.bet == 0: player.place_bet()
                    if player.cash < player.bet:
                        print(f"You have ${player.cash:,.2f}, you don't have enough cash to bet ${player.bet}")
                        input("Press enter to continue.")
                        continue
                    player.cash -= player.bet
                    print(f"You bet ${player.bet}. You now have ${player.cash:,.2f} remaining.")
                    player.cash += game.play_straight(player.bet)
                
                elif menu_selection == '2':
                    player.place_bet()
                    continue
                elif menu_selection == '3':
                    player.display_cash()
                elif menu_selection == '4':
                    print("If the winning numbers match in the same order, you win 150x your bet.")
                elif menu_selection == '5':
                    print("Returning to main menu.")
                    input("Press enter to continue.")
                    break
                input("Press enter to continue.")
            del game
        
        # Play Box
        elif menu_selection == '2':
            game = classes.BoxMode()

            while True:
                if player.cash <= 0:
                    print(f"You have ${player.cash:,.2f}. You do not have enough money to play.")
                    print("Returning to Main Menu.")
                    input("Press Enter to continue.")
                    break
            
                functions.display_game_menu(2)
                player.display_bet()

                menu_selection = input("\n> ")
                
                if menu_selection == '1':
                    if player.bet == 0: player.place_bet()
                    if player.cash < player.bet:
                        print(f"You have ${player.cash:,.2f}, you don't have enough cash to bet ${player.bet}")
                        input("Press enter to continue.")
                        continue
                    player.cash -= player.bet
                    print(f"You bet ${player.bet}. You now have ${player.cash:,.2f} remaining.")
                    player.cash += game.play_box(player.bet)
                
                elif menu_selection == '2':
                    player.place_bet()
                    continue
                elif menu_selection == '3':
                    player.display_cash()
                elif menu_selection == '4':
                    print("If the winning numbers match in any order, you win 50x your bet.")
                elif menu_selection == '5':
                    print("Returning to main menu.")
                    input("Press enter to continue.")
                    break
                input("Press enter to continue.")
            del game

        # Play Straight/Box
        elif menu_selection == '3':
            game = classes.StraightBoxMode()

            while True:
                if player.cash <= 0:
                    print(f"You have ${player.cash:,.2f}. You do not have enough money to play.")
                    print("Returning to Main Menu.")
                    input("Press Enter to continue.")
                    break
            
                functions.display_game_menu(3)
                player.display_bet()

                menu_selection = input("\n> ")
                
                if menu_selection == '1':
                    if player.bet == 0: player.place_bet()
                    if player.cash < player.bet:
                        print(f"You have ${player.cash:,.2f}, you don't have enough cash to bet ${player.bet}")
                        input("Press enter to continue.")
                        continue
                    player.cash -= player.bet
                    print(f"You bet ${player.bet}. You now have ${player.cash:,.2f} remaining.")
                    player.cash += game.play_straight_box(player.bet)
                
                elif menu_selection == '2':
                    player.place_bet()
                    continue
                elif menu_selection == '3':
                    player.display_cash()
                elif menu_selection == '4':
                    print("If winning numbers are an exact match, win 75x your bet.",
                          "Or if the winning numbers match in any order, win 25x your bet.")
                elif menu_selection == '5':
                    print("Returning to main menu.")
                    input("Press enter to continue.")
                    break
                input("Press enter to continue.")
            del game

        # Add Funds
        elif menu_selection == '4':
            player.add_funds()
            input("Press enter to continue.")

        # See Rules
        elif menu_selection == '5':
            functions.display_rules()
            input("Press enter to continue.")

        # Quit
        elif menu_selection == '6':
            print("Thank you for playing!")
            break
    
    del player


main()
