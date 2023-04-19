from collections import deque

class Pile:
    def __init__(self):
        self.deck = deque()

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return str(self.deck)

    def __getitem__(self,i):
        return self.deck[i]

    def mpt(self):
        return len(self.deck) == 0

    def add(self,e):
        self.deck.append(e)

    def rem(self):
        try:
            return self.deck.pop()
        except IndexError:
            return "IndexError: La pile est vide"

    def clear(self):
        for k in range(len(self.deck)):
            self.deck.pop()