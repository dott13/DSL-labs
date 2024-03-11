from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
def visualize(fa, file_name):
    dot = Digraph(comment= "Finite Automata")

    for state in fa.states:
        if state in fa.final_states:
            dot.attr('node', shape="doublecircle")
        else:
            dot.attr('node', shape="circle")
        dot.node(state)

    for (state, symbole), next_states in fa.transitions.items():
        for next_state in next_states:
            dot.edge(state, next_state, label=symbole)
    
    dot.attr('node', shape='none')
    start = 'start'
    dot.node(start, label='')
    dot.edge(start, fa.start_state)

    dot.render(file_name, view=True)
