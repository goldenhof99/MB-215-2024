import unittest  # Import the unittest framework

class TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        """Test that checks if 4 equals 4 (this will pass)"""
        self.assertEqual(4, 4)

    def test_decrement(self):
        """Test that checks if 3 equals 4 (this will fail intentionally)"""
        self.assertEqual(3, 4)

if __name__ == '__main__':
    unittest.main()
