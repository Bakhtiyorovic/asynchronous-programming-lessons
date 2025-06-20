import asyncio
from asyncio import gather

"""
#Simple coroutine
async def Hello():
    print('Hello buddy')
    await asyncio.sleep(3)
    print('lets start')


asyncio.run(Hello())#doin the event loop

#Multple coroutines

async def Coroutine1():
    print('First coroutine started')
    await asyncio.sleep(2)
    print('First corotine ended')

async def Corotine2():
    print('Second corotine started')
    await asyncio.sleep(2)
    print('Second corotine ended')

async def main():
    await asyncio.gather(Coroutine1(), Corotine2())

asyncio.run(main())

"""

#Task
"""
async def work(n):
    await asyncio.sleep(n)
    print(f'{n} second job is done!')

async def main():
    task1 = asyncio.create_task(work(2))
    task2 = asyncio.create_task(work(3))
    await task1
    await task2

asyncio.run(main())
"""
