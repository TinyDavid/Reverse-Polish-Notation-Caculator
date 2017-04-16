#!/usr/bin/env python

import operator
import math

class RPNCaculator(object):
    """
    Class object RPNCaculator with Reverse Polish Notation calculation,
    based on http://en.wikipedia.org/wiki/Reverse_Polish_notation,
    only supports two operands and then an operator, have the following properties:
    
    Attributes:
        operators: A basic operators dictionary, whose values is a list contain oprators, oppsite oprators and operands number.
                   eg: the value of '+' is consist of operator.add, the opposite operator.sub and operands number 2.
                   It can expand with more operators for more complex caculator.
    
    Methods:
        mainMethod: ask user to input numbers and operators, and pass the input(space-split) to the caculate function, 
                    which will return a tuple to valueStackResult, instructionStackResult, 
                    and print valueStackResult with space-separated and 10 decimal places.
        caculate: caculate the result from the input of mainMethod, return the result as a tuple.
        warningMessage: return a warning message when exception happens.
    """
    operators = { '+': [operator.add,operator.sub,2],
            '-': [operator.sub,operator.add,2],
            '*': [operator.mul,operator.truediv,2],
            '/': [operator.truediv,operator.mul,2],
            'sqrt': [math.sqrt,math.pow,1],
            'undo':['undo',None,0],
            'clear':['clear',None,0]
    }
    
    def __init__(self):
        """
        Init two instance variables:
        valueStack (a list store numbers) and 
        instructionStack (a list store the caculated operators and the first operand)
        """
        self.valueStack = []
        self.instructionStack= []

    def warningMessage(self, token, position):
        """return warning message with operator and position when exception"""
        return 'operator %s (position: %d): insufficient parameters' % (token, position)


    def caculate(self, tokens):
        """
        Loop each token from input.
        1, when token is 'clear':
            Remove all items from valueStack and instructionStack.
        2, when token is 'undo':
            Undo the previous operation, it can undo till valueStack is empty.
        3, when token is in '+-*/sqrt'
            Pop their parameters off the valueStack, and append their results back to the valueStack
            Append the last operator and first operand to the instructionStack
        4, when token is number:
            Append float(token) to valueStack and append None to instructionStack.
        The function will return a tuple which contains valueStack and instructionStack.    
        """
        position = 0
        firstOperand = None
        secondOperand = None
        for token in tokens:
            position=position+len(token)+1
            if token in self.operators:
                if token =='clear':
                    self.valueStack = []
                    self.instructionStack = []
                elif token =='undo':
                    try:
                        lastInstruction = self.instructionStack.pop()
                        if lastInstruction is None:
                            self.valueStack.pop()
                        else:                
                            lastStack = self.valueStack.pop()
                            if lastInstruction[0]=="sqrt":
                                secondStack = self.operators[lastInstruction[0]][1](lastStack,2)
                                self.valueStack.append(secondStack)
                            else:
                                secondStack = self.operators[lastInstruction[0]][1](lastStack,lastInstruction[1])
                                self.valueStack.append(secondStack)
                                self.valueStack.append(lastInstruction[1])
                    except IndexError as err:
                        raise IndexError(err)
                else:
                    try:
                        if self.operators[token][2] == 1:
                            firstOperand = self.valueStack.pop()
                            self.valueStack.append(self.operators[token][0](firstOperand))                    
                        elif self.operators[token][2] == 2:
                            try:
                                firstOperand = self.valueStack.pop()
                            except:
                                firstOperand = None
                            try:
                                secondOperand = self.valueStack.pop()
                            except:
                                secondOperand = None
                            self.valueStack.append(self.operators[token][0](secondOperand, firstOperand))
                        self.instructionStack.append([token,firstOperand])
                    except ZeroDivisionError as err:
                        raise ZeroDivisionError(err)
                    except ValueError as err:
                        raise ValueError(err)
                    except:
                        if firstOperand is None and secondOperand is None:
                            self.valueStack = []
                        elif secondOperand is None:
                            self.valueStack.append(firstOperand)
                        elif firstOperand is not None and secondOperand is not None:
                            self.valueStack.append(secondOperand)
                            self.valueStack.append(firstOperand)
                        print(self.warningMessage(token, position-1))
                        break
            else:            
                try:
                    self.valueStack.append(float(token))
                    self.instructionStack.append(None)
                except ValueError:
                    raise ValueError('Error: input should be only real numbers or %s.' % ''.join(self.operators.keys()))
        return self.valueStack, self.instructionStack
        
    def mainMethod(self):
        """
        While loop to ask user to input numbers and operators, and pass the input(space-split) to the caculate function, 
        assign returned tuple to valueStackResult, instructionStackResult, 
        and print valueStackResult with space-separated and 10 decimal places.
        You can input 'quit','q', or 'exit' to quit the programe
        """
        while True:
            expression = input('')
            if expression in ['quit','q','exit']:
                break
            elif len(expression)==0:
                continue
            valueStackResult, instructionStackResult = self.caculate(expression.split())
            print("stack: ", end="")
            for value in valueStackResult:
                print("%.10f"%value, end=" ")
            print("")
            #print("instructionStackResult:%s"%instructionStackResult)


if __name__ == '__main__':
    """Create a new instance RPNCaculator, and invoke the entry function mainMethod"""
    RPNCaculator().mainMethod()    





















    