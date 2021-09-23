import collections
from typing import Final

EPSILON: Final[str] = 'epsilon'


def nested_dict():
    return collections.defaultdict(nested_dict)


def read_data(file: str):
    f = open(file, 'r')
    alphabet: list[str] = f.readline().split('=')[1].removesuffix('\n').split(',')
    states: list[str] = f.readline().split('=')[1].removesuffix('\n').split(',')
    initial_state: str = f.readline().split('=')[1].removesuffix('\n')
    final_states: list[str] = f.readline().split('=')[1].removesuffix('\n').split(',')

    f.readline()  # 'transicoes'
    transitions = nested_dict()

    for line in f:
        transition = line.removesuffix('\n').split(',')
        transitions[transition[0]][transition[1]] = transition[2]

    print('alphabet:', end='')
    print(alphabet)
    print('states:', end='')
    print(states)
    print('initial_state:' + initial_state)
    print('final_states:', end='')
    print(final_states)
    print('transitions')
    print(transitions)

    f.close()


if __name__ == '__main__':
    read_data('input.txt')
