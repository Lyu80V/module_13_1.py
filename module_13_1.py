import time
import asyncio

async def start_strongman(name, power):           # name - имя силача, power - подъёмная мощность
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        number = i + 1                            # number - Номер шара
        await asyncio.sleep(12/power)
        print(f'Силач {name} поднял {number}')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():                      #  Имитация соревнований по поднятию шаров Атласа

    entrant_1 = asyncio.create_task(start_strongman('Pasha', 3))
    entrant_2 = asyncio.create_task(start_strongman('Denis', 4))
    entrant_3 = asyncio.create_task(start_strongman('Michael', 6))

    await entrant_1
    await entrant_2
    await entrant_3

asyncio.run(start_tournament())