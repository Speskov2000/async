from time import sleep

# Round Robin

# iter string
def gen1(s):
    for i in s:
        yield i

# iter numbers
def gen2(n):
    for i in range(n):
        yield i 

# iter numbers reverse
def gen3(n):
    for i in range(n):
        yield n-i 


tasks = []
g1 = gen1('ABCDEFG')
tasks.append(g1)
g2 = gen2(3)
tasks.append(g2)
g3 = gen3(10)
tasks.append(g3)

def loop():
    while tasks:
        sleep(0.5)
        task = tasks.pop(0)
        try:
            i = next(task)
            print(f'{task.__name__} - {i}')
            tasks.append(task)
        except StopIteration:
            print(f'Event loop has completed the generator "{task.__name__}"')


if __name__ == '__main__':
    loop()
