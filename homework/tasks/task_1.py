from asyncio import Task
from typing import Callable, Coroutine, Any
import asyncio


async def f():
    return 2 + 2

async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):
        # YOUR CODE GOES HERE
        t = asyncio.create_task(f())
    elif isinstance(f, Task):
        # YOUR CODE GOES HERE
        t = asyncio.create_task(f())
    elif isinstance(f, Coroutine):
        # YOUR CODE GOES HERE
        t = asyncio.create_task(f())
    else:
        raise ValueError('invalid argument')
    await t

if __name__ == '__main__':
    asyncio.run(await_my_func(f))
