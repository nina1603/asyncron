import asyncio
from typing import Coroutine, Callable

async def func(i):
    await asyncio.sleep(0.0001 * i)
    if i == 3:
        try:
            await asyncio.sleep(i)
        except asyncio.CancelledError:
            print(f"I'm performing too long")
    return i**2

async def limit_execution_time(coro: Coroutine, max_execution_time: float) -> None:
    # Функция принимает на вход корутину, которую необходимо запустить, однако иногда она выполняется
    # слишком долго, это время необходимо ограничить переданным на вход количеством секунд.
    #
    # Тест проверяет, что каждая переданная корутина была запущена, и все они завершились за заданное
    # время.
    #
    # YOUR CODE GOES HERE
    async with asyncio.timeout(max_execution_time):
        await coro


async def limit_execution_time_many(*coros: Coroutine, max_execution_time: float) -> None:
    # Функция эквивалентна limit_execution_time, но корутин на вход приходит несколько.
    #
    # YOUR CODE GOES HERE
    done, pending = await asyncio.wait(coros, timeout=max_execution_time)
    results = [t.result for t in done]
    for t in pending:
        t.cancel()


async def create_coros(f: Callable, values: list[int]) -> list[Coroutine]:
    tasks = [asyncio.create_task(f(value)) for value in values]
    await limit_execution_time_many(*tasks, max_execution_time=2)

if __name__ == '__main__':
    values = list(range(1, 7))
    asyncio.run(create_coros(func, values))
