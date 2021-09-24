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

    def __dfs(self, state: str, chain: str, n: int, through: list[str]) -> bool:
        accept = False
        state_print = (' | ' * n) + state + ('({})'.format(','.join(through)) if through else '')

        if len(chain) == n:  # ended processing chain
            accept = state in self.final_states
            print(state_print + ': ' + ('Accept' if accept else 'Reject'))
        else:
            symbol = chain[n]

            if not self.transitions[state][symbol]:  # crash
                print(state_print + ': Reject (Crash)')
            else:
                print(state_print)
                for s in self.transitions[state][symbol]:
                    accept |= self.__dfs(s, chain, n + 1, [])

        for s in self.transitions[state][FiniteAutomaton.EPSILON]:  # empty chain transitions
            if s not in through:  # avoid empty chain transitions loop
                accept |= self.__dfs(s, chain, n, through + [state])

        return accept

    def process(self, chain) -> bool:
        return self.__dfs(self.initial_state, chain, 0, [])
