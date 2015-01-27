import sys
import time


def main(duration):
    for remaining in range(duration, 0, -1):
        print('Remaining: ', remaining)
        time.sleep(1)


if __name__ == '__main__':
    duration = int(sys.argv[1]) if len(sys.argv) == 2 else 5
    main(duration)
