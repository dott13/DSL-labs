#Variant 23
#Q = {q0,q1,q2},
#∑ = {a,b},
#F = {q2},
#δ(q0,a) = q0,
#δ(q0,a) = q1,
#δ(q1,b) = q2,
#δ(q0,b) = q0,
#δ(q2,b) = q2,
#δ(q1,a) = q0.
from finite_automata import *
from graph import *

nfa = FiniteAutomata(
    states=['0', '1', '2'],
    alphabet=['a', 'b'],
    transitions={
        ('0', 'a'): ['0', '1'],
        ('1', 'a'): ['0'],
        ('0', 'b'): ['0'],
        ('1', 'b'): ['2'],
        ('2', 'b'): ['2']
    },
    start_state='0',
    final_states=['2']
)

print("Is our NFA Deterministic:")
print(is_deterministic(nfa))
#visualize(nfa, 'nfa')

print("\nNFA to DFA:")
dfa = ndf_to_dfa(nfa)
#visualize(dfa, 'dfa')
print(dfa)

reg = to_regular_grammar(nfa)
print("\nNFA to Regular Grammar:")
for state, prods in reg.items():
    for prod in prods:
        print(f"{state} -> {prod}")
