import requests
from time import time, monotonic


# ---------------------------- PART 1 ----------------------------
# ----------------------------- Sync -----------------------------


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))

    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    t0 = monotonic()
    url = 'https://loremflickr.com/320/240'

    for i in range(10):
        write_file(get_file(url))

    print(monotonic() - t0)


if __name__ == '__main__':
    main()
