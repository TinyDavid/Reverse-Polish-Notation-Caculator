import unittest
import rpn_caculator
import math

class TestRNPCaculatorBadInput(unittest.TestCase):

    def setUp(self):
        """ Setting up for the test """
        pass
    
    def tearDown(self):
        """ Cleaning up after the test """
        pass
    
    def testInvalidInput(self):
        self.assertRaises(ValueError, rpn_caculator.RPNCaculator().caculate, 's')
    
    def testZeroDivision(self):
        self.assertRaises(ZeroDivisionError, rpn_caculator.RPNCaculator().caculate, '1 0 /'.split())
        
    def testNegativeSqrt(self):
        self.assertRaises(ValueError, rpn_caculator.RPNCaculator().caculate, '-1 sqrt'.split())
    
    def testInsufficientParameters(self):
        actualValueStack, actualInstructionStack = rpn_caculator.RPNCaculator().caculate('1 2 3 * 5 + * * 6 5'.split())   
        expectedValueStack = [11.0]
        self.assertEqual(actualValueStack, expectedValueStack)
    
    def testUndoWithInsufficientParameters(self):
        self.assertRaises(IndexError, rpn_caculator.RPNCaculator().caculate, '1 2 3 * 5 undo undo undo undo undo undo'.split())

class TestRNPCaculatorCorrectInput(unittest.TestCase):

    def setUp(self):
        """ Setting up for the test """
        pass
    
    def tearDown(self):
        """ Cleaning up after the test """
        pass

    def testNumbersStack(self):
        actualValueStack, actualInstructionStack = rpn_caculator.RPNCaculator().caculate('5 4 3 2'.split())   
        expectedValueStack = [float(5),float(4),float(3),float(2)]
        self.assertEqual(actualValueStack, expectedValueStack)
    
    def testOperatorSqrt(self):
        actualValueStack, actualInstructionStack = rpn_caculator.RPNCaculator().caculate('2 sqrt'.split())   
        expectedValueStack = [math.sqrt(float(2))]
        self.assertEqual(actualValueStack, expectedValueStack)
    
    def testOperatorAdd(self):
        actualValueStack, actualInstructionStack = rpn_caculator.RPNCaculator().caculate('5 2 +'.split())   
        expectedValueStack = [float(5+2)]
        self.assertEqual(actualValueStack, expectedValueStack)
    
    def testOperatorSub(self):
        actualValueStack, actualInstructionStack = rpn_caculator.RPNCaculator().caculate('5 2 -'.split())   
        expectedValueStack = [float(5-2)]
        self.assertEqual(actualValueStack, expectedValueStack)
        
    def testOperatorMul(self):
        actualValueStack, actualInstructionStack = rpn_caculator.RPNCaculator().caculate('1 2 3 4 5 * * * '.split())   
        expectedValueStack = [float(1), float(5*4*3*2*1)]
        self.assertEqual(actualValueStack, expectedValueStack)
    
    def testOperatorDiv(self):
        actualValueStack, actualInstructionStack = rpn_caculator.RPNCaculator().caculate('7 12 2 /'.split())   
        expectedValueStack = [float(7), float(12/2)]
        self.assertEqual(actualValueStack, expectedValueStack)
        
    def testMixOperators(self):
        actualValueStack, actualInstructionStack = rpn_caculator.RPNCaculator().caculate('1 2 3 * 5 + 7 / -'.split())   
        expectedValueStack = [float(1-(2*3+5)/7)]
        self.assertEqual(actualValueStack, expectedValueStack)
    
    def testOperatorClear(self):
        actualValueStack, actualInstructionStack = rpn_caculator.RPNCaculator().caculate('2 sqrt clear'.split())
        self.assertEqual(len(actualValueStack),0)
    
    def testOperatorUndo(self):
        actualValueStack, actualInstructionStack = rpn_caculator.RPNCaculator().caculate('5 4 3 2 undo undo * 5 * undo'.split())
        expectedValueStack = [float(20),float(5)]
        self.assertEqual(actualValueStack, expectedValueStack)
    
        
if __name__ == '__main__':
    unittest.main()