# Reverse Polish Notation Caculator
Command-line based RPN calculator, based on [http://en.wikipedia.org/wiki/Reverse_Polish_notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation),
only supports two operands and then an operator

## Intro
The calculator waits for user input and expects to receive strings containing whitespace
separated lists of numbers and operators.
 
Numbers are pushed on to the stack.  Operators operate on numbers that are on the stack.
 
Available operators are `+`, `-`, `*`, `/`, `sqrt`, `undo`, `clear`
 
Operators pop their parameters off the stack, and push their results back onto the stack.
 
- The `clear` operator removes all items from the stack.

- The `undo` operator undoes the previous operation.  "undo undo" will undo the previous two operations.

- `sqrt` performs a square root on the top item from the stack

- `pow` returns the top item from the stack power 2

- The `+`, `-`, `*`, `/` operators perform addition, subtraction, multiplication and division respectively on the top two items from the stack. 
 
After processing an input string, the calculator displays the current contents of the stack as a space-separated list. Numbers are stored on the stack to at least 15 decimal places of precision, but displayed to 10 decimal places (or less if it causes no loss of precision).
 
If an operator cannot find a sufficient number of parameters on the stack, a warning is displayed:
 
`operator <operator> (position: <pos>): insufficient parameters`

After displaying the warning, all further processing of the string terminates and the current state of the stack is displayed.


## Requirements

- Implemented and tested using Python 3.5.0

- Tests require unittest(Python Unit testing framework)


## Usage

Unzip the file tech_programming_test_rpn.zip in the destination directory with secured password "anz_p2ssword":
README.md
rpn_caculator.py
test_rpn_caculator.py


- Run:
1. change to destination directory: `cd dir(destination directory)` 
2. Run the caculator: `python rpn_caculator.py`
3. Input the numbers or operators into the Command-line and Enter: `5 2 -`
4. Output will print the result in the Command-line: stack: 3.0000000000
5. Can continue test with other input, input 'quit','q', or 'exit' can quit the programe.

- Test:
1. Run the unit test: `python test_rpn_caculator.py -v`
2. The common-line will output the test result:
   testInsufficientParameters (__main__.TestRNPCaculatorBadInput) ... operator * (p
        osition: 15): insufficient parameters
        ok
        testInvalidInput (__main__.TestRNPCaculatorBadInput) ... ok
        testNegativeSqrt (__main__.TestRNPCaculatorBadInput) ... ok
        testUndoWithInsufficientParameters (__main__.TestRNPCaculatorBadInput) ... ok
        testZeroDivision (__main__.TestRNPCaculatorBadInput) ... ok
        testMixOperators (__main__.TestRNPCaculatorCorrectInput) ... ok
        testNumbersStack (__main__.TestRNPCaculatorCorrectInput) ... ok
        testOperatorAdd (__main__.TestRNPCaculatorCorrectInput) ... ok
        testOperatorClear (__main__.TestRNPCaculatorCorrectInput) ... ok
        testOperatorDiv (__main__.TestRNPCaculatorCorrectInput) ... ok
        testOperatorMul (__main__.TestRNPCaculatorCorrectInput) ... ok
        testOperatorSqrt (__main__.TestRNPCaculatorCorrectInput) ... ok
        testOperatorSub (__main__.TestRNPCaculatorCorrectInput) ... ok
        testOperatorUndo (__main__.TestRNPCaculatorCorrectInput) ... ok

        ----------------------------------------------------------------------
        Ran 14 tests in 0.016s

        OK
