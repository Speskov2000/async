import asyncio
from time import monotonic, time
import aiohttp

# ---------------------------- PART 2 ----------------------------
# ----------------------------- Async -----------------------------


async def get_file(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_file(data)


def write_file(data):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))

    with open(filename, 'wb') as file:
        file.write(data)


async def main():
    url = 'https://loremflickr.com/320/240'
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(10):
            tasks.append(asyncio.create_task(get_file(url, session)))
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = monotonic()
    asyncio.run(main())

    print(f'{monotonic()-t0}')
