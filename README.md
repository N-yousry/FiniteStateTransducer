# FiniteStateTransducer

A finite state transducer that operates just like a DFA but also outputs a character at each transition that may be used to interact

_Explanation of Symbols used_

o ∑ is a finite set of input symbols

o O is a finite set of output symbols

o Q is a finite set of states.

o f : Q x ∑ → Q is the “next state” function. 

o g : Q x ∑ → O is the “output” function. 

o 𝑞0∈ Q is the start state
