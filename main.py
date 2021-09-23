from finite_automaton import FiniteAutomaton


def read_data(file: str):
    f = open(file, 'r')
    fa = FiniteAutomaton()

    fa.alphabet = set(f.readline().split('=')[1].removesuffix('\n').split(','))
    fa.states = set(f.readline().split('=')[1].removesuffix('\n').split(','))
    fa.initial_state = f.readline().split('=')[1].removesuffix('\n')
    fa.final_states = set(f.readline().split('=')[1].removesuffix('\n').split(','))

    f.readline()  # reading 'transicoes'
    for line in f:
        transition = line.removesuffix('\n').split(',')
        fa.transitions[transition[0]][transition[2]].append(transition[1])

    f.close()

    return fa


if __name__ == '__main__':
    finite_automaton: FiniteAutomaton = read_data('afn2ex1.txt')
    input_chain: str = input('Input chain: ')
    finite_automaton.process(input_chain)
