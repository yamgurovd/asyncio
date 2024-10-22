import asyncio

def print_0():
    return "Hello World 0"


async def print_1():
    return "Hello World 1"


def main_0():
    print("Начало 0")
    tasks = [print_0() for _ in range(500)]
    print(tasks)

async def main_1():
    print("Начало 1")
    tasks = [print_1() for _ in range(500)]
    results = await asyncio.gather(*tasks)
    print(f"Вывод {results}")

main_0()
asyncio.run(main_1())
