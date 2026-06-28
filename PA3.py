"""
Program Name: Die Roll Game
Author: Freda Acquah
Purpose: Rolling dice with different side counts and prints the results.
Starter Code: No starter code was used.
Date: June 28, 2026
"""
from random import randint


class Die:
    # Represents a single die with a configurable number of sides
    def __init__(self, sides=6):
        # store the number of sides for this die
        self.sides = sides

    def roll_die(self):
        # Print a random roll result between 1 and the number of sides
        print(randint(1, self.sides))


# Create 6-sided die and roll it 10 times
print("10 rolls of a 6-sided die:")
d6 = Die()
for roll_num in range(10):
    d6.roll_die()

# Create a 10-sided die and roll it 10 times
print("\n10 rolls of a 10-sided die:")
d10 = Die(sides=10)
for roll_num in range(10):
    d10.roll_die()

# Create a 20-sided die and roll it 10 times
print("\n10 rolls of a 20-sided die:")
d20 = Die(sides=20)
for roll_num in range(10):
    d20.roll_die()
