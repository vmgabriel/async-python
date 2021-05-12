"""test async functions"""

# Libraries
import unittest
import asyncio

# Modules
from src import async_func


class TestAsync(unittest.TestCase):
    """Test Async Class"""
    def test_async_return_hello_world(self):
        """Test verify asyn return of hello world Function"""
        x = asyncio.run(async_func.hello_world())
        self.assertEqual(x, 'Hello World', "Should be hello world")


class TestAsyncCalculator(unittest.TestCase):
    """Test Calculator Async"""

    def setUp(self):
        """Set configuration"""
        self.acalc = async_func.ACalculator()

    def test_async_sum(self):
        """test async sum"""
        val1, val2 = 5, 4
        leg = asyncio.run(self.acalc.sum(val1, val2))
        self.assertEqual(leg, val1 + val2, "Should be sum value")

    def test_async_rest(self):
        """test async rest data"""
        val1, val2 = 5, 4
        leg = asyncio.run(self.acalc.rest(val1, val2))
        self.assertEqual(leg, val1 - val2, "Should be rest value")


    def test_async_mult(self):
        """test async mult data"""
        val1, val2 = 5, 4
        leg = asyncio.run(self.acalc.mult(val1, val2))
        self.assertEqual(leg, val1 * val2, "Should be mult value")


    def test_async_div(self):
        """test async div data"""
        val1, val2 = 5, 4
        leg = asyncio.run(self.acalc.div(val1, val2))
        self.assertEqual(leg, val1 / val2, "Should be div value")


    def test_async_div_zero(self):
        """test asybc div data"""
        val1, val2 = 6, 0
        leg = asyncio.run(self.acalc.div(val1, val2))
        self.assertEqual(leg, 0, "Should be div value zero")


    def test_async_operation(self):
        """test async operation"""
        val1, val2, op = 2, 3, '+'
        fun = asyncio.run(self.acalc.operation(val1, val2, op))
        self.assertEqual(fun, 5, "Should be operation sum")
        op = '-'
        fun = asyncio.run(self.acalc.operation(val1, val2, op))
        self.assertEqual(fun, -1, "Should be operation rest")
        op = '*'
        fun = asyncio.run(self.acalc.operation(val1, val2, op))
        self.assertEqual(fun, 6, "Should be operation multiply")
        op = '/'
        fun = asyncio.run(self.acalc.operation(val1, val2, op))
        self.assertEqual(fun, val1 / val2, "Should be operation division")
