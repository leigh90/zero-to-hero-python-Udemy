import unittest
import cap

# create the testing class
class TestCap(unittest.TestCase):
    # the test class inherits from unittest's testcase class

    # create the method to test various functions
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == "__main__":
    unittest.main()