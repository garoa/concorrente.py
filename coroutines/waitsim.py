from queue import PriorityQueue
import itertools

def show(customer, time, activity):
    print('[%3d] %s: %s' % (time, customer, activity))

def visit(customer, arrival):
    time = arrival
    show(customer, time, 'arrives at branch')
    time = yield
    show(customer, time, 'waiting in line')
    time = yield
    show(customer, time, 'doing transactions')
    time = yield
    show(customer, time, 'leaves branch')

def enqueue(line, visit, time):
    visit.send(time)
    line.put(visit)

def serve(line, clock):
    while not line.empty():
        visit = line.get()
        visit.send(next(clock))

def main(clock):
    visit_a = visit('A', next(clock))
    visit_b = visit('B', next(clock))
    next(visit_a)
    next(visit_b)
    line = Queue()
    enqueue(line, visit_a, next(clock))
    enqueue(line, visit_b, next(clock))
    serve(line, clock)

if __name__ == '__main__':
    main(itertools.count())
