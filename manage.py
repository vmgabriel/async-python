
"""Action Run The Application"""

# Libraries
# import tornado.ioloop
import time
import asyncio
from random import random


# Modules
# from src import make_app


async def multi(a, b):
    time.sleep(2)
    return a * b
    # raise Exception('A + 1')


async def process(a, b):
    print('proces start')
    time.sleep(2)
    mult = await multi(a, b)
    print('mult data - ', mult)
    print('this is the data 2')
    time.sleep(2)
    return a + b


async def process_2(a, b):
    print('this is the data')
    time.sleep(2)
    mult = a * b
    print('mult data - ', mult)
    print('this is the data 2')
    time.sleep(2)
    return a + b


async def process_posibility_error(a, b):
    data = int(1 + random() * 10)
    print('data - ', data)
    time.sleep(data)
    if data % 2 == 0:
        return a + b
    else:
        raise Exception('Data is not odd')


async def data_all():
    first_data = [random() for _ in range(3)]
    second_data = [random() for _ in range(3)]
    as_data = [
        asyncio.create_task(process_posibility_error(a, b))
        for a, b in zip(first_data, second_data)
    ]
    return asyncio.gather(*as_data, return_exceptions=True)


def proc_after_proc(inter):
    print('type-', type(inter))
    if isinstance(inter, Exception):
        print('Exception data - ', inter)
        return 0
    return inter



# if __name__ == '__main__':
#     print('Server Listen : localhost:8888')
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    try:
        print('data process')
        # data = asyncio.run(process(2, 3)) # Condicion
        # data = asyncio.run(process_2(4, 3))
        data = asyncio.run(data_all())
        print('this is the out - ', data)
        print('type of data - ', type(data))

        print('is Future', asyncio.isfuture(data))
        x = data.result()
        print('x result - ', x)
        print('x is list', type(x))
        print('x result prc - ', list(map(proc_after_proc, x)))

        # proc = list(map(lambda x: x.done(), data))
        # print('sol of proc - ', proc)
    except Exception as exc:
        print('[ERROR] - ', exc)
