from _collections import deque


class deques:
    def __init__(self):
        self.items = deque()

    def add_front(self, item):
        """
        Add items you inserted in front index. Forceful shift in other index. Time complexity O(n).
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """
        Add items you inserted in last index of deque. Time complexity O(1).
        """
        self.items.append(item)

    def remove_front(self):
        """
        Remove item at index 0 form deque. Time complexity O(n).
        """
        if self.items:
            return self.items.popleft()
        return None

    def remove_rear(self):
        """
        Remove item at last index from deque. Time complexity O(n).
        """
        return self.items.pop()


my_deque = deques()
my_deque.add_front(1)
my_deque.add_front(0)
my_deque.add_rear(2)
my_deque.add_rear(3)
print(f'My deque is {my_deque.items}')
my_deque.remove_front()
print(f'After removing first item in deque, it looks like {my_deque.items}')
my_deque.remove_rear()
print(f'After removing last item in deque, it looks like {my_deque.items}')
