import asyncio


async def custom_coro():
    print("Hello")
    await asyncio.sleep(1)
    print("World")



asyncio.run(custom_coro())