from enum import Enum

from app.models.blackjack_models import BlackjackTurn

"""
player_id - The ID of this blackjack player,
player_max_hand - The max hand value before being bust,
dealer_stop - The dealers hand value when the dealer stops pulling cards,
dealer_hand - The current cards in the dealers hand,
current_hand - The current cards in the players hand,
played_cards - All previously played cards before shuffling,
deck_amount - The amount of decks used by the dealer
"""

example_blackjack_turn = {
    "player_id": "bob",
    "player_max_hand": "21",
    "dealer_stop": "17",
    "dealer_hand": ["AH"],
    "current_hand": ["7D", "2S"],
    "played_cards": ["7D", "AH", "2S"],
    "deck_amount": "2",
}


class TurnAction(Enum):
    HIT = "Hit"
    STAND = "Stand"


def possible_cards(cards: list[str]) -> list[list[int]]:
    """
    Returns all numbers that can be made with the cards in the hand.
    """
    possible_numbers = []
    for card in cards:
        if card[0] == "A":
            # Ace can be 1 or 11
            possible_numbers.append([1, 11])
        elif card[0] in ["J", "Q", "K"]:
            possible_numbers.append([10])
        else:
            # All other cards are their number value
            possible_numbers.append([int(card[0])])
    return possible_numbers


def max_hand_value(possible_numbers: list[list[int]]) -> int:
    """
    Calculate the maximum hand value
    """
    max_hand = 0
    for hand in possible_numbers:
        for number in hand:
            if max_hand + number > 21:
                continue
            max_hand += number
    return max_hand


def take_turn(blackjack_turn: BlackjackTurn) -> TurnAction:
    """
    Receives all data needed to decide what action to take,
    should return either TurnAction.HIT or TurnAction.STAND.
    :param blackjack_turn:
    :return:
    """

    cards = possible_cards(blackjack_turn.current_hand)
    max_hand = max_hand_value(cards)

    if max_hand > int(blackjack_turn.dealer_stop):
        # If the players max hand is greater than the dealers stop value,
        # the player should stand.
        return TurnAction.STAND

    return TurnAction.HIT
