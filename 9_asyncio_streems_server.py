import asyncio


async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')
    print("Connection from", addr)

    while True:
        request = await reader.read(4096)
        if not request:
            break
        else:
            message = request.decode().replace('\n', "")
            response = f'> Server response to "{message}"\n'.encode()
            writer.write(response)
            await writer.drain()

    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, 'localhost', 5000)

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(server())
