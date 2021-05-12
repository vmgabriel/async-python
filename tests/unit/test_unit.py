"""test unit"""

# Libraries
import unittest

# Modules
from src import main


class TestSum(unittest.TestCase):
    """Test Sum Class"""
    def test_sum(self):
        """Test Sum Function"""
        self.assertEqual(main.suma(3, 4), 7, "Should be 7")
