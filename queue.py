class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Function to add item in first index or simply enqueue.
        Time complexity is O(n) or linear. If item is added in first index all next items should be shifted by one.
        Time depends upon list length.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        It removes and return the first element which is added in a list or last item in list.
        Time complexity is O(1) or constant since it works on last index only.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """
        Return last element in list or front-most in queue  that is going to be deleted next.
        Time complexity is O(1)
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Return length of the queue. Time complexity O(1).
        """
        return len(self.items)

    def is_empty(self):
        """
        Check if queue is empty or not. O(1).
        """
        if self.items:
            return 'not empty!'
        return 'empty!'


my_queue = queue()
my_queue.enqueue('apple')
my_queue.enqueue('banana')
my_queue.enqueue('orange')
print(f'My queue order is {my_queue.items}.')
print(f'Removing the first item you inserted in list that is {my_queue.dequeue()}.')
print(f'The item going to be deleted next is {my_queue.peek()}.')
print(f'My queue order is {my_queue.items}.')
print(f'The size of queue is {my_queue.size()}.')
print(f'My queue status is {my_queue.is_empty()}.')
