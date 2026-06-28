"""
Program Name: Match Coins Game
Author: Freda Acquah
Purpose: Runs a two-player coin matching game and reports each player's coins.
Starter Code: No starter code was used.
Date: June 28, 2026
"""

from player import Player


def main():
    # Create two Player objects for the game
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Ask the user whether to start playing
    play_again = input("Do you want to play? (y/n): ")

    # Continue rounds while the user agrees to play again
    while play_again == "y" or play_again == "Y":
        # Each player tosses their own Coin object
        player1.toss_coin()
        player2.toss_coin()

        # Get the current side of each player's coin
        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        # Show the results of both coin tosses
        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        # If the sides match, player1 wins the round and player2 loses a coin
        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"{player1.get_name()} won the round.")
        else:
            # If the sides do not match, player2 wins the round
            player2.win_coin()
            player1.lose_coin()
            print(f"{player2.get_name()} won the round.")

        # Display each player's current wallet balance
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        # End the game early if either player runs out of coins
        if player1.get_wallet() == 0:
            print(f"{player1.get_name()} has 0 coins. Game over!")
            print(f"{player1.get_name()} is the loser.")
            break
        elif player2.get_wallet() == 0:
            print(f"{player2.get_name()} has 0 coins. Game over!")
            print(f"{player2.get_name()} is the loser.")
            break

        # Ask the user if they want to continue playing
        play_again = input("\nDo you want to play again? (y/n): ")

    # Print final summary once the game ends
    print("\nFinal Results:")
    print(f"{player1.get_name()} finished with {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} finished with {player2.get_wallet()} coins.")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} finished with more coins.")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} finished with more coins.")
    else:
        print("Both players finished with the same number of coins.")
        print("It's a draw!")


if __name__ == "__main__":
    main()
