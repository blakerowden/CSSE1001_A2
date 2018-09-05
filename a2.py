#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

import random

__author__ = "Blake Rowden s4427634"


class Card(object):
    def __init__(self, number, colour):
        self._number = number
        self._colour = colour

    def get_number(self):
        return self._number

    def get_colour(self):
        return self._colour

    def set_number(self, number):
        self._number = number

    def set_colour(self, colour):
        self._colour = colour

    def get_pickup_amount(self):
        pass  # Returns the amount of cards the next player should pickup

    def matches(self, card):
        if self.get_colour() == card.get_colour() or \
           self.get_number() == card.get_number():
            return True
        else:
            return False

    def play(self, player, game):
        pass  # Perform a special card action. The base Card class has no special action.


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
