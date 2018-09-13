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
        return 0

    def matches(self, card):
        if self.get_colour() == card.get_colour() or \
           self.get_number() == card.get_number():
            return True
        else:
            return False

    def play(self, player, game):
        pass

    def __str__(self):
        return "Card({0}, {1})".format(self.get_number(),
                                       self.get_colour())

    def __repr__(self):
        return self.__str__()


class ReverseCard(Card):

    def play(self, player, game):
        game.reverse()


class SkipCard(Card):

    def play(self, player, game):
        game.skip()


class Pickup2Card(Card):

    def get_pickup_amount(self):
        return 2

    def play(self, player, game):
        game.get_turns().peak().get_deck().add_cards(game.pickup_pile.pick(2))


class Pickup4Card(Card):

    def get_pickup_amount(self):
        return 4

    def play(self, player, game):
        game.get_turns().peak().get_deck().add_cards(game.pickup_pile.pick(4))


class Deck(object):
    def __init__(self, starting_cards=None):
        if starting_cards is None:
            self._deck = []
        else:
            self._deck = starting_cards

    def get_cards(self):
        return self._deck

    def get_amount(self):
        return len(self.get_cards())

    def shuffle(self):
        random.shuffle(self._deck)

    def pick(self, amount: int=1):
        pick_list = []
        for _ in range(amount):
            if self.get_amount() != 0:
                pick_list.append(self._deck.pop())
        return pick_list

    def add_card(self, card):
        self._deck.append(card)

    def add_cards(self, cards):
        for card in cards:
            self._deck.append(card)

    def top(self):
        try:
            return self.get_cards()[len(self.get_cards())]
        except IndexError:
            return None


class Player(object):
    def __init__(self, name):
        self._name = name
        self._deck = Deck()

    def get_name(self):
        return self._name

    def get_deck(self):
        return self._deck

    def is_playable(self):
        raise NotImplementedError

    def has_won(self):
        return self.get_deck().get_amount() == 0

    def pick_card(self, putdown_pile):
        raise NotImplementedError


class HumanPlayer(Player):

    def is_playable(self):
        return True


class ComputerPlayer(Player):

    def is_playable(self):
        return False

    def pick_card(self, putdown_pile):
        for i in self.get_deck().get_cards():
            if i.matches(putdown_pile.top()):
                self.get_deck().get_cards().remove(i)
                return i



def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
