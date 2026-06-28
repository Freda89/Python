"""
Program Name: Match Coins Game - Coin Class
Author: Freda Acquah
Purpose: Defines a Coin class that stores and tosses one coin as Heads or Tails.
Starter Code: No starter code was used.
Date: June 28, 2026
"""

from random import randint


class Coin:
    def __init__(self):
        # Set the initial side of the coin to Heads
        self.__sideup = "Heads"

    def toss(self):
        # Randomly choose a result for the coin toss
        toss_result = randint(0, 1)

        # use an if statement to set the sideup attribute based on the toss result
        if toss_result == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        #Returns the current value of sideup.
        return self.__sideup
