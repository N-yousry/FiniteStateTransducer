# FiniteStateTransducer

A finite state transducer that operates just like a DFA but also outputs a character at each transition that may be used to interact

_Formal Description of FST_

**M = (∑, 𝑂, 𝑄, 𝑓, 𝑔, 𝑞0):**

1. ∑ is a finite set of input symbols

2. O is a finite set of output symbols

3. Q is a finite set of states.

4. f : Q x ∑ → Q is the “next state” function. 

5. g : Q x ∑ → O is the “output” function. 

6. 𝑞0∈ Q is the start state


