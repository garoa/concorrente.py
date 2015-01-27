import sys
import asyncio


def show_remaining(duration, loop):
    if not hasattr(show_remaining, 'remaining'):
        show_remaining.remaining = duration

    print('Remaining: ', show_remaining.remaining)
    show_remaining.remaining -= 1
    if show_remaining.remaining:
        loop.call_later(1, show_remaining, duration, loop)
    else:
        loop.stop()


def main(duration):
    loop = asyncio.get_event_loop()
    try:
        loop.call_soon(show_remaining, duration, loop)
        loop.run_forever()
    finally:
        loop.close()


if __name__ == '__main__':
    duration = int(sys.argv[1]) if len(sys.argv) == 2 else 5
    main(duration)
