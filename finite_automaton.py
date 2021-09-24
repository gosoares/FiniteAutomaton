import collections
from typing import Final
import pptree


class FiniteAutomaton:
    EPSILON: Final[str] = 'epsilon'

    def __init__(self):
        self.alphabet: set[str] = set()
        self.states: set[str] = set()
        self.initial_state: str = ''
        self.final_states: set[str] = set()
        self.transitions: dict[str, dict[str, list[str]]] = collections.defaultdict(
            lambda: collections.defaultdict(list))

    def __dfs(self, state: str, chain: str, n: int, through: list[str], parent: pptree.Node) -> bool:
        accept = False
        state_data = state + ('({})'.format(','.join(through)) if through else '')

        if len(chain) == n:  # ended processing chain
            accept = state in self.final_states
            pptree.Node(state_data + ': ' + ('Accept' if accept else 'Reject'), parent)
        else:
            symbol = chain[n]

            if not self.transitions[state][symbol]:  # crash
                pptree.Node(state_data + ': Reject', parent)
            else:
                p_node = pptree.Node(state_data, parent)
                for s in self.transitions[state][symbol]:
                    accept |= self.__dfs(s, chain, n + 1, [], p_node)

        through.append(state)
        for s in self.transitions[state][FiniteAutomaton.EPSILON]:  # empty chain transitions
            accept |= self.__dfs(s, chain, n, through, parent)
        through.pop()

        return accept

    def process(self, chain) -> bool:
        p_root: pptree.Node = pptree.Node('initial')
        accepted = self.__dfs(self.initial_state, chain, 0, [], p_root)

        for p_node in p_root.children:
            pptree.print_tree(p_node)

        return accepted
