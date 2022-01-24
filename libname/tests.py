from main import mainStr
import unittest

class TestCase(unittest.TestCase):
    
    def testMain(self):
        self.assertEqual(mainStr(), "HelloFromMyLib")

if __name__ == '__main__':
    unittest.main()