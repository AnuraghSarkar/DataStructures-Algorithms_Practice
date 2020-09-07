class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Accepts items and add it in a list.
        Run time to this method is O(1) or constant time since appending at end of list happens in constant time.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and Returns last item of list.
        Run time is O(1) or constant time since it pops items indexes at right most position.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """
        This method return last item in list. Time complexity is constant complexity O(1).
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        This method returns length of list if there is any items else print None. Time complexity is constant i.e. O(1).
        """
        if self.items:
            return len(self.items)
        return None

    def is_empty(self):
        """
        This method checks if list is empty or not. Time complexity is constant.
        """
        return self.items == []


my_stack = stack()
my_stack.push('apple')
my_stack.push('orange')
my_stack.push('banana')
my_stack.push('orange')
my_stack.push('grape')
my_stack.push('guava')
print(f'Before removing last item, current stack is: {my_stack.items}')
print(f'Removing {my_stack.pop()}')
print(f'After removing last item from list: {my_stack.items}')
print(f'Next item to pop is {my_stack.peek()}')
print(f'Size of current list is {my_stack.size()}')
print(f'List is empty? {my_stack.is_empty()}')
