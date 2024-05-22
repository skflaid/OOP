import unittest
import ForTest

class TestBase(unittest.TestCase):

    def testHelloWorld(self):
        b = ForTest.Base()
        self.assertEqual(b.helloWorld(), "HelloWorld!")

    def testNumSquare(self):
        b = ForTest.Base()
        self.assertEqual(b.NumSquare(), 100)

    def testTwice(self):
        b = ForTest.Base()
        b.getT("I am")
        self.assertEqual(b.twice(), "I amI am")

if __name__ == '__main__':
    unittest.main()