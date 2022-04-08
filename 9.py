import socket
import asyncio
# from select import select

loop = asyncio.get_event_loop()


async def accept_connection():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()

    while True:
        client_socket, addr = return(await server_socket.accept())
        print("Connection from", addr)
        task = asyncio.ensure_future(send_message(client_socket))


async def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = "> My response\n".encode()
        client_socket.send(response)
    else:
        client_socket.close()


async def main():
    task = asyncio.ensure_future(accept_connection())

    await asyncio.gather(task)


if __name__ == "__main__":
    loop.run_until_complete(main())
    loop.close()
