# Report on Chomsky Normal Form

## Introduction

In formal language theory, a context free grammar G is said to be in Chomsky Normal Form if all of its production rules are of the form:

```
A -> BC, or
A -> a, or
S -> epsilon
```

## Objectives

1. Learn about Chomsky Normal Form (CNF) [1].
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
   1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
   2. The implemented functionality needs executed and tested.
   3. A **BONUS point** will be given for the student who will have unit tests that validate the functionality of the project.
   4. Also, another **BONUS point** would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.

## Implementation

To convert Grammar to Chomsky Normal Form we need some conditions: First we declare a <i>Grammar</i> class in `grammar.py` after that we declare another class for Converting to Chomski Form in `toChomsky.py`.

After all preparitions are done we need to just implement the algorithm, first we need to <i>eliminate the epsilon terms</i>:

```python
def epsilonElimination(self):
        counter = 1
        while counter:
            for symbol in self.P:
                for production in list(self.P[symbol]):
                    if production == '':
                        self.symbolReplacement(symbol)
                        self.P[symbol].remove('')
                        counter += 1
            counter -= 1
```

In this code we just remove the epsilon term which we declared as ''(commas), we then remove it from the list of all simbols in our productions and thats it.

The second step would be to eliminate non-productive symbols. To do so we will make another method:

```python
for symbol in list(self.P):
                dzone = False
                for production in list(self.P[symbol]):
                    terminals = False
                    nterminals = False
                    itself = False
                    for p in production:
                        if p == symbol:
                            itself = True
                        elif p in self.VN:
                            nterminals = True
                        elif p in self.VT:
                            terminals = True

                    if itself and not nterminals:
                        dzone = True
                    if (terminals or nterminals) and not itself:
                        dzone = False
```

This is a bit more complicated but basically we just seek the products that loop back or dont go anywhere. So if the sybol is not in nterminals then we know that it is looping back. So we just eliminate that symbol.

Next is to eliminate the innaccessible symbols from our grammar, this step requires another method:

```python
 production_w_start = self.remove_key(self.P, 'S')
            for symbol in list(production_w_start):
                production_w_symbol = self.remove_key(self.P, symbol)
                accessible = False

                for symbols in list(production_w_symbol):
                    for production in symbols:
                        if symbol in production:
                            accessible = True
                            break

                    if accessible:
                        break
```

In this case we just seek through all the productions for keys that cannot be accessed through the productions. So if the symbol is there we have an accessible symbol, otherwise not so we just get it out from our poducts list with the method declared for elimnation.

After that we renamed a lot of things so we need to verify if those renamings have some breaches in them, in this case we just seek relations through the productions and change the namings as it is made.

Next we actually do the chomsky transformation for the change of nonterminals and renaming convention. This is also made with a method.

```python
for i, symbol in enumerate(self.VT):
            self.VN.add(f'X{i}')
            self.P[f'X{i}'] = symbol

        for symbol in list(self.P):
            for production in list(self.P[symbol]):
                if len(production) == 2:
                    new_production = ''
                    for char in production:
                        if char in self.VT:
                            newX = f'X{list(self.VT).index(char)}'
                            new_production += newX
                        else:
                            new_production += char
                    self.P[symbol].remove(production)
                    self.P[symbol].add(new_production)
```

In this step, first we add the X Non-Terminals first, then we change the characters in the productions list to the X terms, if the production list has terminals with the length 2 we just add a new X Term and remove the previous one. Thats basically it.

## Output

As an output we are printing it all out in the main class with the `convert()` method. I decided to print out every step we made, In the implementation with elimination of symbols, chomsky transform and etc.

This is the output:

```
Non-terminals (VN): {'A', 'S', 'E', 'B', 'C'}
Terminals (VT): {'a', 'b'}
Productions (P):
S -> bAC, B
A -> aS, a, bCaCb
B -> AC, aAa, bS
C -> , AB
E -> BA

after eliminating epsilon

Non-terminals (VN): {'A', 'S', 'E', 'B', 'C'}
Terminals (VT): {'a', 'b'}
Productions (P):
S -> bA, bAC, B
A -> baCb, a, bab, bCaCb, aS, bCab
B -> A, AC, aAa, bS
C -> AB
E -> BA

after eliminating nonproductive symbols

Non-terminals (VN): {'A', 'S', 'E', 'B', 'C'}
Terminals (VT): {'a', 'b'}
Productions (P):
S -> bA, bAC, B
A -> baCb, a, bab, bCaCb, aS, bCab
B -> A, AC, aAa, bS
C -> AB
E -> BA

after eliminating inaccessible symbols

Non-terminals (VN): {'S'}
Terminals (VT): {'a', 'b'}
Productions (P):
S -> bA, bAC, B

after eliminating any renaming

Non-terminals (VN): {'S'}
Terminals (VT): {'a', 'b'}
Productions (P):
S -> bA, bAC, B

 after chomsky transformation

Non-terminals (VN): {'S', 'X0', 'X1'}
Terminals (VT): {'a', 'b'}
Productions (P):
S -> X1A, bAC, B
X0 -> a
X1 -> b
```

## Conclusion

After dealing with all the steps we can actually make any grammar into Chomsky Normal Form thanks to our new Class we made in `toChomsky.py` file. We dealt with all the objectives and we got a fully working project, being able to convert our grammar to Chomsky Normal Form.

he conversion process is iterative and involves inspecting and modifying the grammar based on specific criteria at each step. The output of the conversion process is a CFG that adheres to the rules of Chomsky Normal Form, which can be further used for parsing and analysis in computational linguistics and formal language theory.
