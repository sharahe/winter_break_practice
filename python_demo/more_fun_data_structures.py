# several of these are stored in the collections
import collections

def demo_minipulating_lists():
    """If you ever want to sort a list"""
    print("Demo on minimplulating lists")
    a = [-1, 2, 4, 7, 89, 5, 3, 234, 5, 5]
    print("Normal a: {}".format(a))

    b = sorted(a)
    print("Sorted a: {}".format(b))

    c = reversed(a)
    print("Reversed a: {}".format(c))
    print(
        "uhoh, sometimes things don't return what you think they will. This time it "
        "returned an object (more efficient in memory). You can force it back into a"
        "list by calling list(your_thing)")
    print("Reversed a forced to be a list: {}".format(list(c)))


def demo_queues():
    """Queues are fun because you can quickly add (append) and pull off (pop) things from them.
    Priority queues (queues) are another thing that will be important later (they sort themselves).
    Honestly you can use a list for an unsorted queue, but performance-wise, using a queue is more
    efficient and it shows that you know the difference

    There is another library called "queues" which supposedly does both a normal and a priority
    queue but it doesn't come with python like 'collections' so I usually use that"""
    print("")
    q = collections.deque()
    q.append(10)
    q.append(20)
    q.append(30)
    print("OG queue: {}, length: {}".format(q, len(q)))
    print("")
    num = q.popleft()
    print("popped number: {}, remaining queue: {}".format(num, q))
    print(
        "You see that when you pop a number, it is removed from the queue and if you want to keep "
        "it (not always true), you must put it somewhere")
    print("they are often used in conjunction with while-loops")

    print("")
    while len(q) > 0:
        num = q.popleft()
        print("popped number: {}, remaining queue: {}".format(num, q))


if __name__ == '__main__':
    demo_queues()
    demo_minipulating_lists()
