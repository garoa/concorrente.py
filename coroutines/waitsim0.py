from queue import PriorityQueue
import itertools

def show(customer, time, activity):
    print('[%3d] %s: %s' % (time, customer, activity))

def visit(customer, arrival):
    time = arrival
    show(customer, time, 'waiting in line')
    time = yield
    show(customer, time, 'doing business')
    time = yield
    show(customer, time, 'leaves branch')

def enqueue(line, visit, time):
    visit.send(time)
    line.put(visit)

def serve(line, clock):
    while not line.empty():
        visit = line.get()
        visit.send(next(clock))

def main():
    events = PriorityQueue()
    for i in range(1, 8):
        visit_coro = visit('Customer #%d' % i, i)
        next(visit_coro)  # prime
        events.put((i, visit_coro))
    while not events.empty():
        timestamp, visit_coro = events.get()





if __name__ == '__main__':
    main()
