import asyncio
from asyncio import gather
import time
"""

#
async def Hello():
    print('Hello buddy')
    await asyncio.sleep(3)
    print('lets start')


asyncio.run(Hello())#doin the event loop

#
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

#
async def work(n):
    await asyncio.sleep(n)
    print(f'{n} second job is done!')

async def main():
    task1 = asyncio.create_task(work(2))
    task2 = asyncio.create_task(work(3))
    await task1
    await task2

asyncio.run(main())


#
async def vazifa_a():
    await asyncio.sleep(3)
    print("Vazifa A bajarildi." )

async def vazifa_b():
    await asyncio.sleep(1)
    print("Vazifa B bajarildi." )

async def main():
    start_time = time.time()
    await asyncio.gather(vazifa_a(), vazifa_b())
    print(f"Umumiy vaqt: {time.time() - start_time:.2f} soniya")

asyncio.run(main())

#
async def kalkulyator(a, b):
    await asyncio.sleep(1)
    print(f"{a} va {b}ning yigi'indisi {a+b}ga teng!")

async def main():
    task = asyncio.create_task(kalkulyator(2, 3))
    await task

asyncio.run(main())



#
async def sekin_vazifa():
    await asyncio.sleep(5)
    print( "Sekin vazifa bajarildi.")

async def main():
    try:
        result = await asyncio.wait_for(sekin_vazifa(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print('Sekin vazifa bajarilmadi')

if __name__ == '__main__':
    asyncio.run(main())

"""

