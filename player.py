"""
Program Name: Match Coins Game - Player Class
Author: Freda Acquah
Purpose: Defines a Player class with a name, wallet, and Coin object to toss.
Starter Code: No starter code was used.
Date: June 28, 2026
"""

from coin import Coin


class Player:
    #set the initial values for the name, wallet, and coin attributes
    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()
 # Tosses the coin and updates the sideup attribute of the Coin object.
    def toss_coin(self):
        self.__coin.toss()
# Returns the current value of sideup from the Coin object.
    def get_coin_side(self):
        return self.__coin.get_sideup()
#Adds 1 to the wallet
    def win_coin(self):
        self.__wallet += 1
#Subtracts 1 from the  wallet
    def lose_coin(self):
        self.__wallet -= 1
 #Returns the current value of wallet.
    def get_wallet(self):
        return self.__wallet

#Returns the value of name.
    def get_name(self):
        return self.__name
