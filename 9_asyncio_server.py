import asyncio
import socket


async def handle_client(client_socket):
    loop = asyncio.get_event_loop()

    while True:
        request = await loop.sock_recv(client_socket, 4096)
        if not request:
            break
        else:
            message = request.decode().replace('\n', "")
            response = f'> Server response to "{message}"\n'.encode()
            await loop.sock_sendall(client_socket, response)

    print('Close the connection')
    client_socket.close()


async def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()
    server_socket.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        client_socket, addr = await loop.sock_accept(server_socket)
        print("Connection from", addr)
        loop.create_task(handle_client(client_socket))


if __name__ == "__main__":
    asyncio.run(server())
