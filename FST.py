### FST Class
class FiniteStatetransducer:
    #############################(∑,𝑂, 𝑄, 𝑓, 𝑔, 𝑞0):############################
    
    # (∑= inputsymbols , O=outputsymbols, Q= finite set of states,F=next state, G=output, Q0=start state)"""
    def __init__(self):     
          
        self.inputsymbols = list()    # ∑= inputsymbols 
        self.outputsymbols = list()   # O=outputsymbols
        self.statesQ = list()         # Q= finite set of states 
        self.nextstate= dict()        # F=next state
        self.OutputFn= dict()         # G=output  
        self.Qo_startstate = None     # Q0=start state

    
    def setstartstate(self, stringin):
        #Validation 
        if self.Qo_startstate is not None :
         return ("You Already Entered a Start State")
        self.Qo_startstate = stringin

        
    def createstates(self, stringin):
        #Validation 
        if stringin in self.statesQ:
            return ("Already Exists")


    def setoutputsymbols(self, stringin):
        #Validation 
        if stringin in self.outputsymbols:
           return ("Already Exists")
        self.outputsymbols.append(stringin)

    def setinputsymbols(self, stringin):
        #Validation 
        if stringin in self.inputsymbols:
           return ("Already Exists")
        self.inputsymbols.append(stringin)   

    def setnextstate(self,current_state, letter, next ):
        if current_state not in self.statesQ or next not in self.statesQ:
            return ("State Doesn't Exist")
            
        if letter not in self.inputsymbols:

            return ("InVaild Input Symbol, Doesn't Belong to Language")  
        
        mainList= list([current_state,letter])
        mainTuple=tuple(mainList)
        #Valiadation if i repatead a tranistion 
        if mainTuple in self.nextstate:
            return ("Tranistion Exists")

        self.nextstate[mainTuple]= next

        # Letter is input , Value : output 
    def setofOutputFn(self, current_state, letter, value):
        #Valiadation to see if the user entered a state that doesnt exist
        if current_state not in self.statesQ: 
            return ("State Doesn't Exist")
        #Valiadation to see if a symbol entered a state that doesnt exist    
        if letter not in self.inputsymbols:
            return ("InVaild Input Symbol, Doesn't Belong to Language")

        if value not in self.outputsymbols:
            return ("InVaild Value, Doesn't To Output List")

        mainList= list([current_state,letter])
        mainTuple=tuple(mainList)
        #Valiadation if i repatead an ouput value
        if mainTuple in self.OutputFn:
            return ("Output Already Exists")


    def checkString(self, s):
        currentS = self.Qo_startstate
        nextS = None
        outS = ""
        for i in s:
            #Vaildation
            if i not in self.inputsymbols:
                return ("String Doesn't Belong to the Language")
            #Search in Dictroinary
            List_s = list([currentS, i])
            newTuple=tuple(List_s)
            nextS= self.nextstate[newTuple]
            outS += self.OutputFn[newTuple]
            currentS= nextS
            print(nextS)
            print(outS)
            print("*****************")
        print(outS)
      
        return
    
### TEST CASES

# Test Case 1
# Lecture Example 1
def test_case_1():

    Test=FiniteStatetransducer()
    Test.setstartstate("q0")  
    Test.createstates("q1")

    Test.setinputsymbols("a")
    Test.setinputsymbols("b")

    Test.setoutputsymbols("0")
    Test.setoutputsymbols("1")


    Test.setnextstate("q0", "a", "q0")
    Test.setnextstate("q0", "b", "q1")
    Test.setnextstate("q1", "a", "q1")
    Test.setnextstate("q1", "b", "q1")

    Test.setofOutputFn("q0", "a", "1")
    Test.setofOutputFn("q0", "b", "0")
    Test.setofOutputFn("q1", "a", "0")
    Test.setofOutputFn("q1", "b", "0")

    Test.checkString("aababba")


# Test Case 2
# Lecture Example 2
def test_case_2():
    Test=FiniteStatetransducer()

    Test.setstartstate("q0")  
    Test.createstates("q1")

    Test.setinputsymbols("a")
    Test.setinputsymbols("b")

    Test.setoutputsymbols("0")
    Test.setoutputsymbols("1")

    Test.setnextstate("q0", "a", "q1")
    Test.setnextstate("q0", "b", "q1")
    Test.setnextstate("q1", "a", "q0")
    Test.setnextstate("q1", "b", "q1")

    Test.setofOutputFn("q0", "a", "1")
    Test.setofOutputFn("q0", "b", "1")
    Test.setofOutputFn("q1", "a", "0")
    Test.setofOutputFn("q1", "b", "1")

    Test.checkString("aabbab")


# Test Case 3
# Example From Sheet
def test_case_3():
    Test=FiniteStatetransducer()

    Test.setstartstate("q0")  
    Test.createstates("q1")
    Test.createstates("q2")

    Test.setinputsymbols("a")
    Test.setinputsymbols("b")
    Test.setinputsymbols("c")

    Test.setoutputsymbols("0")
    Test.setoutputsymbols("1")

    Test.setnextstate("q0", "a", "q0")
    Test.setnextstate("q0", "b", "q1")
    Test.setnextstate("q0", "c", "q2")
    Test.setnextstate("q1", "a", "q1")
    Test.setnextstate("q1", "b", "q1")
    Test.setnextstate("q1", "c", "q0")
    Test.setnextstate("q2", "a", "q2")
    Test.setnextstate("q2", "b", "q1")
    Test.setnextstate("q2", "c", "q0")


    Test.setofOutputFn("q0", "a", "0")
    Test.setofOutputFn("q0", "b", "1")
    Test.setofOutputFn("q0", "c", "0")
    Test.setofOutputFn("q1", "a", "1")
    Test.setofOutputFn("q1", "b", "1")
    Test.setofOutputFn("q1", "c", "1")
    Test.setofOutputFn("q2", "a", "1")
    Test.setofOutputFn("q2", "b", "0")
    Test.setofOutputFn("q2", "c", "0")

    Test.checkString("aabbcc")


#test_case_3()



    
