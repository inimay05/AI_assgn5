import random
import math

class Node:

    def __init__(self, state):
        self.state = state
        self.visits = 0
        self.wins = 0

    def uct(self, total_visits):

        if self.visits == 0:
            return float('inf')

        return (
            self.wins / self.visits
            + math.sqrt(
                2 * math.log(total_visits)
                / self.visits
            )
        )

root = Node("root")

children = [
    Node("A"),
    Node("B"),
    Node("C")
]

for _ in range(100):

    selected = max(
        children,
        key=lambda c: c.uct(
            root.visits + 1
        )
    )

    reward = random.choice([0,1])

    selected.visits += 1
    selected.wins += reward

    root.visits += 1

for child in children:

    print(
        child.state,
        "Visits:",
        child.visits,
        "Wins:",
        child.wins
    )
