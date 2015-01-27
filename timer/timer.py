import sys
import asyncio


@asyncio.coroutine
def show_remaining(duration):
    for remaining in range(duration, 0, -1):
        print('Remaining: ', remaining)
        yield from asyncio.sleep(1)


def main(duration):
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(show_remaining(duration))
    finally:
        loop.close()

if __name__ == '__main__':
    duration = int(sys.argv[1]) if len(sys.argv) == 2 else 5
    main(duration)
