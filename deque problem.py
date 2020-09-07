from _collections import deque


def palindrome_checker(word):
    """
    Function to check if a word is palindrome or not. Time complexity is O(n) removing first index make other index to shift front
    by 1 index.
    """
    my_deque = deque(word)
    while len(my_deque) > 1:
        first_item = my_deque.popleft()
        last_item = my_deque.pop()
        if first_item != last_item:
            return False
        return True
    return False


print(palindrome_checker('ss'))
