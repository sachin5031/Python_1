import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self):
        self.original_deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.deck = self.original_deck.copy()

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        if self.deck:
            return self.deck.pop()
        else:
            raise ValueError("The deck is empty. No cards to draw.")

    def reset_deck(self):
        self.deck = self.original_deck.copy()
        self.shuffle()

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return f"Deck of {len(self.deck)} cards"


# Example usage
deck = Deck()
print("Original deck:")
print(deck.deck)

print("\nShuffling deck...")
deck.shuffle()
print(deck.deck)

print("\nDrawing 5 cards:")
for _ in range(5):
    print(deck.draw_card())

print(f"\nRemaining cards in deck: {len(deck)}")

print("\nResetting deck...")
deck.reset_deck()
print(deck.deck)
print(f"\nRemaining cards in deck: {len(deck)}")
