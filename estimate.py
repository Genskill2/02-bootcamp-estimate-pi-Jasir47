import math
import unittest
import random

def wallis(n):
   list3 = []
   for i in range(1,n+1):
     r = (4*i**2)/((4*i**2)-1) 
     list3.append(r)
   result = 1
   for x in list3:
      result = result*x
   return(2*result)
   

def monte_carlo(i):
   lists1 = [] 
   lists2 = [] 
   for num in range(i) :
       
       x = random.random()
       y = random.random()
       distance = ((x**2)+(y**2))**(1/2)
       

       if distance <= 1:
        lists1.append(1) 
       else:
        lists2.append(1)
        
   print(4*(len(lists1)/(len(lists1)+len(lists2))))
   return(4*(len(lists1)/(len(lists1)+len(lists2))))

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
