import collections
from typing import Final


class FiniteAutomaton:
    EPSILON: Final[str] = 'epsilon'

    def __init__(self):
        self.alphabet: set[str] = set()
        self.states: set[str] = set()
        self.initial_state: str = ''
        self.final_states: set[str] = set()
        self.transitions: dict[str, dict[str, list[str]]] = collections.defaultdict(
            lambda: collections.defaultdict(list))

    def __dfs(self, state: str, chain: str, n: int):
        state_print = (' | ' * n) + state

        if len(chain) == n:  # ended processing chain
            print(state_print + ': ' + ('Accept' if state in self.final_states else 'Reject'))
        else:
            symbol = chain[n]

            if not self.transitions[state][symbol]:  # crash
                print(state_print + ': Reject')
            else:
                print(state_print)
                for s in self.transitions[state][symbol]:
                    self.__dfs(s, chain, n + 1)

        for s in self.transitions[state][FiniteAutomaton.EPSILON]:  # empty chain transitions
            self.__dfs(s, chain, n)

    def process(self, chain):
        return self.__dfs(self.initial_state, chain, 0)
