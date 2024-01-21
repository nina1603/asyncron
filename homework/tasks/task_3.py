import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def process_task(task: Ticket):
    await asyncio.sleep(0.001)
    return task.number, task.key

async def create_coroutines(tasks: list[Ticket]):
    #result = [a async for a in tasks]
    tasks = [asyncio.create_task(process_task(task)) for task in tasks]
    return await coroutines_execution_order(asyncio.gather(*tasks))

async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    # Необходимо выполнить все полученные корутины, затем упорядочить их результаты
    # по полю number и вернуть строку, состоящую из склеенных полей key.
    #
    # Пример:
    # r1 = Ticket(number=2, key='мыла')
    # r2 = Ticket(number=1, key='мама')
    # r3 = Ticket(number=3, key='раму')
    #
    # Результат: 'мамамылараму'
    #
    # YOUR CODE GOES HERE
    # loop = asyncio.get_event_loop()
    # for coro in coros:
    # tasks = loop.create_task(coro)
    # loop.run_until_complete(tasks)

    pairs = await coros
    pairs_sorted = sorted(pairs, key=lambda x: x[0])
    res = ""
    for pair in pairs_sorted:
        res += pair[1]

    print(res)

if __name__ == '__main__':
    r1 = Ticket(number=2, key='мыла')
    r2 = Ticket(number=1, key='мама')
    r3 = Ticket(number=3, key='раму')
    asyncio.run(create_coroutines([r1, r2, r3]))

