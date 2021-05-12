"""Async function"""

# Libraries
from time import sleep


async def hello_world():
    """Print hello world"""
    sleep(3)
    return 'Hello World'


class ACalculator:
    """Class Async Calculator"""
    async def sum(self, a, b):
        """function sum a + b"""
        sleep(2)
        return a + b

    async def rest(self, a, b):
        """function rest a - b"""
        sleep(2)
        return a - b

    async def mult(self, a, b):
        """function mult a * b"""
        sleep(2)
        return a * b

    async def div(self, a, b):
        """function div a / b"""
        sleep(2)
        if b == 0:
            return 0
        return a / b

    async def operation(self, val1, val2, op):
        """function operation"""
        sleep(2)
        if op == '+':
            return await self.sum(val1, val2)
        if op == '-':
            return await self.rest(val1, val2)
        if op == '*':
            return await self.mult(val1, val2)
        if op == '/':
            return await self.div(val1, val2)
