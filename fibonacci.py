import unittest

def fibonacci(num):
    resultado=0
    if num ==0: #caso base
        return resultado
    if num == 1:
        return 1
    if num >= 2:
        return fibonacci(num-2)+fibonacci(num-1) 
class test_conteo_vocales(unittest.TestCase):
    def test_0(self):
        resultado=fibonacci(0)
        self.assertEqual(resultado,0)
        
    def test_1(self):
        resultado=fibonacci(1)
        self.assertEqual(resultado,1)
        
    def test_2(self):
        resultado=fibonacci(2)
        self.assertEqual(resultado,1)
        
    def test_3(self):
        resultado=fibonacci(3)
        self.assertEqual(resultado,2)
        
    def test_4(self):
        resultado=fibonacci(4)
        self.assertEqual(resultado,3)
        
    def test_5(self):
        resultado=fibonacci(5)
        self.assertEqual(resultado,5)
        
    def test_6(self):
        resultado=fibonacci(6)
        self.assertEqual(resultado,8)
        
    def test_7(self):
        resultado=fibonacci(7)
        self.assertEqual(resultado,13)
        
    def test_8(self):
        resultado=fibonacci(8)
        self.assertEqual(resultado,21)
        
    def test_11(self):
        resultado=fibonacci(11)
        self.assertEqual(resultado,89) 
    
    def test_12(self):
        resultado=fibonacci(12)
        self.assertEqual(resultado,144)
        
    def test_13(self):
        resultado=fibonacci(13)
        self.assertEqual(resultado,233)   
unittest.main()