import sys
import asyncio

def make_show_remaining(duration):
    remaining = duration

    def show_remaining(loop):
        nonlocal remaining
        print('Remaining: ', remaining)
        remaining -= 1
        if remaining:
            loop.call_later(1, show_remaining, loop)
        else:
            loop.stop()

    return show_remaining


def main(duration):
    loop = asyncio.get_event_loop()
    try:
        loop.call_soon(make_show_remaining(duration), loop)
        loop.run_forever()
    finally:
        loop.close()

if __name__ == '__main__':
    duration = int(sys.argv[1]) if len(sys.argv) == 2 else 5
    main(duration)

