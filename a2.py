#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

import random

__author__ = "Blake Rowden s4427634"


class Card(object):
    """
    A class to represent a basic card in Uno with a number and colour.
    """
    def __init__(self, number, colour):
        """
        Construct a new card based on a number and colour.

        Parameters:
            number (int): The number to set.
            colour (a2_support.CardColour): The colour to set.

        Preconditons:
            0 < number < 10
        """
        self._number = number
        self._colour = colour

    def get_number(self):
        """
        Returns:
            int: the card number.
        """
        return self._number

    def get_colour(self):
        """
        Returns:
            string: The card colour.
        """
        return self._colour

    def set_number(self, number):
        """
        Sets the number value of the card.

        Parameters:
             number (int): The number to set the card.

        Preconditions:
           0 < number < 10
        """
        self._number = number

    def set_colour(self, colour):
        """
        Sets the colour of the card.

        Parameters:
            colour (a2_support.CardColour): The colour to set the card.
        """
        self._colour = colour

    def get_pickup_amount(self):
        """
        Returns:
            (int): The amount of cards the next player should pick up; set at 0 for base card.
        """
        return 0

    def matches(self, card):
        """
        Determines if the next card can be "legally" placed on this card.

        Parameters:
            card (Card): The card that is checked against this card.

        Returns:
             bool: True iff the given card matches this card, against uno rules.
        """
        if self.get_colour() == card.get_colour() or \
                self.get_number() == card.get_number():
            return True
        else:
            return False

    def play(self, player, game):
        """
        Performs a special card action, no action for base card.
        """
        pass

    def __str__(self):
        """
        Returns the string representation of the card.
        """
        return "Card({0}, {1})".format(self.get_number(),
                                       self.get_colour())

    def __repr__(self):
        """
        Same as __str__(self)
        """
        return self.__str__()


class SpecialCard(Card):

    def matches(self, card):
        """
        Determines if the next card can be "legally" placed on this card.

        Parameters:
            card (Card): The card that is checked against this card.

        Returns:
             bool: True iff the given card matches this card, against uno rules.
        """
        if self.get_colour() == card.get_colour() or \
                type(self) == type(card):
            return True
        return False


class ReverseCard(SpecialCard):
    """
    A subclass of Card which reverses order of turns.
    """

    def play(self, player, game):
        """Reverses the order of turns"""
        game.reverse()


class SkipCard(SpecialCard):
    """
    A subclass of Card which skips the turn of the next player.
    """

    def play(self, player, game):
        """Skips the turn of the next player"""
        game.skip()


class Pickup2Card(SpecialCard):
    """
    A subclass of Card which makes the next player pickup two cards.
    """

    def get_pickup_amount(self):
        """
        Returns: 2 (int) The amount of cards the next player should pick up.
        """
        return 2

    def play(self, player, game):
        """
        Makes the next player pickup two cards.

        Parameters:
            player (Player): Player playing the card.
            game (a2_support.UnoGame): Instance of UnoGame being played.
        """
        game.get_turns().peak().get_deck().add_cards(game.pickup_pile.pick(2))


class Pickup4Card(Card):

    def get_pickup_amount(self):
        """
        Returns: 4 (int) The amount of cards the next player should pick up.
        """
        return 4

    def play(self, player, game):
        """
        Makes the next player pickup two cards.

        Parameters:
            player (Player): Player playing the card.
            game (a2_support.UnoGame): Instance of UnoGame being played.
        """
        game.get_turns().peak().get_deck().add_cards(game.pickup_pile.pick(4))

    def matches(self, card):
        """
        Makes the Pickup4Card match with all cards.
        """
        return True


class Deck(object):
    """
    A class containing a collection of ordered Uno cards.
    """
    def __init__(self, starting_cards=None):
        """
        Construct a deck of cards in an ordered list,
        if no starting cards are provided will create an empty deck.

        Parameters:
            starting_cards (list<Card>): List of cards to initialise the deck with.
        """
        if starting_cards is None:
            self._deck = []
        else:
            self._deck = starting_cards

    def get_cards(self):
        """
        Returns:
             list<Card>: A list of current cards in the deck.
        """
        return self._deck

    def get_amount(self):
        """
        Returns:
             int: The amount of cards in the deck.
        """
        return len(self.get_cards())

    def shuffle(self):
        """
        Shuffles the order of the cards in the deck.
        """
        random.shuffle(self._deck)

    def pick(self, amount: int=1):
        """
        Takes the first "amount" of cards off the deck and returns them.

        Parameters:
            amount (int): Number of cards to take from the deck.

        Returns:
            list<Card>: A list containing all cards taken from the deck.
        """
        pick_list = []
        for _ in range(amount):
            if self.get_amount() != 0:
                pick_list.append(self._deck.pop())
        return pick_list

    def add_card(self, card):
        """
        Places a card on the top of the deck.

        Parameters:
            card (Card): A card to be placed on the deck.
        """
        self._deck.append(card)

    def add_cards(self, cards):
        """
        Places a list of cards on the top of the deck.

        Parameters:
            cards (list<Card>): List of cards to add to deck
        """
        for card in cards:
            self._deck.append(card)

    def top(self):
        """
        Peaks at the card on the top of the deck.

        Returns:
            card (Card): The card on the top of the deck.
            None: Returns iff deck is empty.
        """
        try:
            return self.get_cards()[self.get_amount()-1]
        except IndexError:
            return None


class Player(object):
    """
    An abstract class representing a player in a game of Uno.
    """
    def __init__(self, name):
        """
        Construct a player with a name and empty deck.

        Parameters:
            name (string): name of the player.
        """
        self._name = name
        self._deck = Deck()

    def get_name(self):
        """
        Returns:
            string: The players name.
        """
        return self._name

    def get_deck(self):
        """
        Returns:
            list<T>: The list containing the players deck of cards.
        """
        return self._deck

    def is_playable(self):
        """
        Returns:
             bool: True iff player is human.
        """
        raise NotImplementedError

    def has_won(self):
        """
        Returns:
            bool: True iff player has an empty deck and has therefore won.
        """
        return self.get_deck().get_amount() == 0

    def pick_card(self, putdown_pile):
        """
        Selects a card for a computer player to play and removes it from the deck.

        Parameters:
            putdown_pile (Deck): Deck for the automated player to place down card.

        Returns:
            card (Card): Card that matches the top of the putdown_pile, as per Uno rules.
            None: Returns if player is human or no card can be played.
        """
        raise NotImplementedError


class HumanPlayer(Player):
    """
    A human player class that selects cards to play using the GUI.
    """
    def is_playable(self):
        """
        Returns:
            bool: True iff player is human.
        """
        return True

    def pick_card(self, putdown_pile):
        """
        Not used for HumanPlayer
        """
        pass


class ComputerPlayer(Player):
    """
    A computer player class that selects cards to play automatically.
    """
    def is_playable(self):
        """
        Returns:
            bool: True iff player is human.
        """
        return False

    def pick_card(self, putdown_pile):
        """
        Selects a card for a computer player to play and removes it from the deck.

        Parameters:
            putdown_pile (Deck): Deck for the automated player to place down card.

        Returns:
            card (Card): Card that matches the top of the putdown_pile, as per Uno rules.
            None: Returns if player is human or no card can be played.
        """
        for i in self.get_deck().get_cards():
            if i.matches(putdown_pile.top()):
                self.get_deck().get_cards().remove(i)
                return i
        return None


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
