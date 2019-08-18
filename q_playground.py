from trees.Queue import Queue

q = Queue()

q.enq("1")
q.enq("2")
q.enq("3")
q.enq("4")

while (len(q)) is not 0:
    print(q.deq())
