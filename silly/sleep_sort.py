"""
Inspired by::

    #!/bin/bash
    function f() {
        sleep "$1"
        echo "$1"
    }
    while [ -n "$1" ]
    do
        f "$1" &
        shift
    done
    wait

Example usage::

    ./sleepsort.bash 5 3 6 3 6 3 1 4 7

source:
http://dis.4chan.org/read/prog/1295544154/

"""

import sys
import time
import threading

def out(arg):
    n = float(arg)
    threading.Timer(n, print, (arg,), {'end':' '}).start()

for arg in sys.argv[1:]:
    out(arg)

while len(threading.enumerate()) > 1:
    pass

print()
